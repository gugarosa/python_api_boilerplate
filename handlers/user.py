import hashlib

import tornado
from bson import ObjectId

from decorators.auth import auth
from handlers.base import BaseHandler
from models.user import User


class UserHandler(BaseHandler):
    """An user handler defines all the incoming user-related requests
        that can be processed by the API.

    """

    @auth()
    def get(self, user_id):
        """It defines the GET request for this handler.

        Args:
            user_id (int): The user identifier number.

        Returns:
            It will return either 'True' or 'False' along with a 'success' or an 'error' response.

        """

        # Recovering data from database
        query = self.db(User).find_one({'_id': ObjectId(user_id)})

        # Defining the response object
        res = {
            'id': str(query.id),
            'username': query.username,
            'email': query.email
        }

        # Writing back response
        self.write(dict(success=res))

        return True

    @auth()
    def patch(self, user_id):
        """It defines the PATCH request for this handler.

        Args:
            user_id (int): The user identifier number.

        Returns:
            It will return either 'True' or 'False' along with a 'success' or an 'error' response.

        """

        try:
            # Getting authentication object
            res = tornado.escape.json_decode(self.request.body)

            # Getting username
            username = res['username']

            # Encoding password
            password = hashlib.sha256(res['password'].encode()).hexdigest()

            # Also, we need to encode the new password
            new_password = hashlib.sha256(
                res['new_password'].encode()).hexdigest()

        # If patching object was not found, reply with an error
        except:
            # Setting status to bad request
            self.set_status(400)

            # Writing back an error message
            self.write(
                dict(error='Missing either username, password or new password.'))

            return False

        # Performing query in database to check if user exists
        query = self.db(User).find_one(
            {'username': username, 'password': str(password)})

        # If user does not exists
        if not query:
            # Reply with a bad request
            self.set_status(400)

            # Writing an error message
            self.write(dict(error='Invalid credentials.'))

            return False

        # If everything was correct, we can now update its password
        self.db.update_one(query, set={'password': new_password})

        # Writing back response
        self.write(dict(success='Password updated.'))

        return True
