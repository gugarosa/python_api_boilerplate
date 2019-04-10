from yadm import Document, fields


class User(Document):
    """A model that defines what an user looks like.
    
    """

    # Defining colleciton name
    __collection__ = 'users'

    # Defining model attributes
    username = fields.StringField()
    password = fields.StringField()
    key = fields.StringField()
    token = fields.StringField()
