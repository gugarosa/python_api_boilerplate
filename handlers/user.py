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
