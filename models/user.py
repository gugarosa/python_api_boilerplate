from yadm import Document, fields


class User(Document):
    """A model that defines what an user looks like.
    
    """

    # Defining colleciton name
    __collection__ = 'users'

    # Defining model attributes
    name = fields.StringField()
