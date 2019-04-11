import tornado
from bson import ObjectId
import json

from decorators.auth import auth
from handlers.base import BaseHandler
from models.sample import Sample


class SampleHandler(BaseHandler):
    """A sample handler defines all the incoming sample-related requests
        that can be processed by the API.

    """

    @auth()
    def get(self, sample_id):
        """It defines the GET request for this handler.

        Args:
            sample_id (int): The user identifier number.

        """

        # Recovering data from database
        query = self.db(Sample).find_one({'_id': ObjectId(sample_id)})

        # Defining the response object
        res = {
            'id': str(query.id),
            'data': query.data,
            'type': query.type,
            'label': query.label._data,
            'lock': query.lock
        }

        # Writing back response
        self.write(dict(success=res))

    @auth()
    def post(self, sample_id):
        """It defines the POST request for this handler.

        """

        try:
            # Getting registering object
            res = tornado.escape.json_decode(self.request.body)

            # Getting data (sample's input)
            data = res['data']

            # Type of sample (can be 'text', 'ner', 'audio')
            if res['type'] in ['text', 'ner', 'audio']:
                type = res['type']
            else:
                raise Exception

        # If registering object was not found, reply with an error
        except:
            # Setting status to bad request
            self.set_status(400)

            # Writing back an error message
            self.write(dict(error='Missing either input data or correct type.'))

            return False
        
        # Inserts a new sample in the database
        self.db.insert_one(Sample(data=data, type=type))

        # Writes back the response
        self.write(dict(success='New sample registered.'))
