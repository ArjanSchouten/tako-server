from mongoengine import StringField, EmbeddedDocument


class Message(EmbeddedDocument):
    message = StringField(required=True, max_length=50)
