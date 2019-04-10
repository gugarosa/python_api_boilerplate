import hashlib
import random
import string

import jwt
import tornado

from decorators.auth import auth
from handlers.base import BaseHandler
from models.user import User


class RegisterHandler(BaseHandler):
    """A register handler is composed of any related activity according to
        users-related information in the API.

    """

    async def post(self):
        """It defines the POST request for this handler.

        """
        
        #
        res = tornado.escape.json_decode(self.request.body)

        #
        username = res['username']

        #
        h = hashlib.sha256(res['password'].encode())
        password = h.hexdigest()

        #
        token = None

        #
        query = self.db(User).find_one({'username': username})

        #
        if not query:
            #
            key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(30))

            #
            self.db.insert_one(User(username=username, password=password, key=key, token=token))

            #
            self.write(dict(result='New user registered.'))

        #
        else:
            #
            self.set_status(400)

            #
            self.write(dict(result='User already exists.'))
