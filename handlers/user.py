from decorators.auth import auth
from handlers.base import BaseHandler
from models.user import User


class UserHandler(BaseHandler):
    """An user handler is composed of any related activity according to
        users-related information in the API.

    """

    @auth()
    def get(self, user_id):
        """It defines the GET request for this handler.

        Args:
            user_id (int): The user identifier number.

        """

        # Recovering data from database
        query = self.db(User).find_one({'name': user_id})

        # Defining the response object
        res = {
            'id': str(query.id)
        }

        # Need to encode query and serialize with json_util

        # Writing back response
        self.write(dict(result=res))

    def post(self, user_id):
        """It defines the POST request for this handler.

        Args:
            user_id (int): The user identifier number.

        """

        # Creating the user object
        user = User(name=user_id)

        # Inserting into database
        self.db.insert_one(user)

        # Defining the response object
        res = 'User inserted with success.'

        # Writing back response
        self.write(dict(result=res))
