from yadm import Document, fields
from models.user import User


class Sample(Document):
    """A model that defines what a sample looks like.
    
    """

    # Defines the collection name to be used
    __collection__ = 'samples'

    # It is composed by data, data can be whatever
    data = fields.StringField()

    # Also, it needs a type
    type = fields.StringField()

    # A sample will always be labeled in the future
    label = fields.ListField(fields.StringField())

    # It will be labeled by someone in the future as well
    label_by = fields.ReferenceField(User)

    # A lock to block others from using it
    lock = fields.BooleanField(default=0)
