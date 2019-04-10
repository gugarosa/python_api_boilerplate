import configparser
import logging

import pymongo
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from yadm import Database

from handlers.login import LoginHandler
from handlers.register import RegisterHandler
from handlers.user import UserHandler

# Enables logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Gets the logging object
logger = logging.getLogger(__name__)

# Initializes the configuration object and parses it
config = configparser.ConfigParser()
config.read('config.ini')

# Loading constants
PORT = config.get('API', 'PORT')
STRING = config.get('MONGO', 'STRING')
DB = config.get('MONGO', 'DATABASE')


class Server(Application):
    """A class to hold and bootstrap all the application services.

    """

    def __init__(self):
        """It serves as the application initialization method.

        Note that you will need to set your own arguments, handlers and
        default settings from Tornado.

        """

        # You can define your own arguments
        args = {
            'config': config,
            'db': db
        }

        # And also the desired handlers that will handle the requests
        handlers = [
            (r'/api/login', LoginHandler, args),
            (r'/api/register', RegisterHandler, args),
            (r'/api/users/?(?P<user_id>[^\/]+)?', UserHandler, args)
        ]

        # Bootstraping the application class
        Application.__init__(self, handlers, debug=True, autoreload=True)


if __name__ == '__main__':
    # Logging initial information
    logging.info('Trying to connect to database ...')

    # Creating an object to hold desired MongoDB database
    client = pymongo.MongoClient(STRING)
    db = Database(client, DB)

    logging.info(f'Database connected: {db}')

    # Logging important information
    logging.info('Starting server ...')

    # Tries to start a tornado webserver
    try:
        # Logs its port
        logging.info(f'Port: {PORT}')

        # Creates an application
        app = HTTPServer(Server())

        # Servers the application on desired port
        app.listen(PORT)

        # Starts a IOLoop instance
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()
