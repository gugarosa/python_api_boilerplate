import base64
import json
import jwt
from datetime import datetime, timedelta

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    """A handler class is defined by its main possible requests
    and other necessary functions.

    """

    def initialize(self, **kwargs):
        """It servers as the basic initializer of every incoming request.

        """

        # Defining the configuration object
        self.config = kwargs.get('config')

        # Defining the database object
        self.db = kwargs.get('db')

    def set_default_headers(self):
        """Sets the default response headers for an incoming request.

        """

        # Setting CORS-issue related
        self.set_header('Access-Control-Allow-Origin', '*')

        # Only authorized headers should proceed
        self.set_header('Access-Control-Allow-Headers',
                        'x-requested-with, Authorization, Content-type')

        # And only allowed methods
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, OPTIONS, PATCH, DELETE, PUT')

    def get_token(self):
        """Gets the authorization token from the request.

        Returns:
            The requested token.

        """

        # Gathering authorization token
        try:
            token = self.request.headers.get('Authorization').split(' ')[1]
        except:
            token = ''

        return token

    def check_auth(self, token):
        """
        """

        try:
            #
            res = json.loads(base64.b64decode(token.split(".")[1]+"==").decode())
            print(f'Res: {res}')

            #
            token = jwt.decode(token, self.config.get('API', 'SECRET'), algorithms=['HS256'])

            if token:
                print(token)
            else:
                print('Expired')
            print(f'Verify: {token}')
            print(datetime.now())
            print(datetime.fromtimestamp(token['exp']))
            if datetime.utcnow() > datetime.fromtimestamp(token['exp']):
                print('Ok')
            else:
                self.set_status(403)

                return False
            #key = self.cacheServer.get(user)
            #verify = jwt.decode(token, key, algorithms=["HS256"])
        except Exception as e:
            print(e)
            return False
