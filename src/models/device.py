from mongoengine import Document, StringField, ListField, EmbeddedDocumentField

from models.message import Message


class Device(Document):
    device_id = StringField(required=True, max_length=50, primary_key=True)
    receiver_id = StringField(required=True, max_length=50)
    messages = ListField(EmbeddedDocumentField(Message))
