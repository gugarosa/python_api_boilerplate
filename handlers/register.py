import hashlib
import random
import string

import jwt
import tornado

from decorators.auth import auth
from handlers.base import BaseHandler
from models.user import User


class RegisterHandler(BaseHandler):
    """A register handler is used to handle every new register request incoming
        to the API.

    """

    async def post(self):
        """It defines the POST request for this handler.

        """
        
        try:
            # Getting registering object
            res = tornado.escape.json_decode(self.request.body)

            # Recovering username
            username = res['username']

            # Encoding password
            password = hashlib.sha256(res['password'].encode()).hexdigest()

            # Recovering user's email
            email = res['email']
        
        # If registering object was not found, reply with an error
        except:
            # Setting status to bad request
            self.set_status(400)

            # Writing back an error message
            self.write(dict(error='Missing either username, password or email.'))

            return False

        # Tries to find if username is already taken
        query = self.db(User).find_one({'username': username})

        # If username is valid
        if not query:
            # Inserts a new user in the database
            self.db.insert_one(User(username=username, password=password, email=email))

            # Writes back the response
            self.write(dict(success='New user registered.'))

        # If username is not valid
        else:
            # Sets the status as a bad request
            self.set_status(400)

            # And replies an error message
            self.write(dict(error='User already exists.'))
