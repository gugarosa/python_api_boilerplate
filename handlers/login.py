from decorators.auth import auth
from handlers.base import BaseHandler
from models.user import User
import tornado
import hashlib
import jwt
from datetime import datetime, timedelta


class LoginHandler(BaseHandler):
    """An user handler is composed of any related activity according to
        users-related information in the API.

    """

    async def post(self):
        """It defines the POST request for this handler.

        """

        try:
            # Getting authentication object
            res = tornado.escape.json_decode(self.request.body)

        #
        except Exception as e:
            self.write(dict(result=e))

        # Recovering username and password
        username = res['username']

        #
        password = hashlib.sha256(res['password'].encode()).hexdigest()
        
        #
        query = self.db(User).find_one({'username': username, 'password': str(password)})

        #
        if not query:
            #
            self.set_status(403)

            return False

        data = {
            'username': query.username,
            'exp': datetime.utcnow() + timedelta(seconds=3600)
        }

        print(f'Login: {data}')

        encoded = jwt.encode(data, self.config.get('API', 'SECRET'), algorithm='HS256')

        # Writing back response
        self.write(dict(result=encoded.decode()))
