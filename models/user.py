from yadm import Document, fields


class User(Document):
    """A model that defines what an user looks like.
    
    """

    # Defines the collection name to be used
    __collection__ = 'users'

    # An user needs an username
    username = fields.StringField()
    
    # Also, he needs a password
    password = fields.StringField()

    # And finally, an e-mail
    email = fields.StringField()
