from flask import request
from flask_restful import Resource, abort

from models.device import Device
from models.message import Message
from utils import check_firmware_version_header, check_device_id_header


class SendMessageRequest(Resource):
    @check_device_id_header
    def post(self, device_id):
        json = request.get_json(silent=True)
        if json is None or json['message'] is None:
            abort(400)

        # Lookup the device in the database or abort if it isn't found
        device = self.get_device_by_device_id(device_id)
        if device is None:
            abort(404)

        self.save_message_to_receiver(device, Message(message=json['message']))

    @staticmethod
    def save_message_to_receiver(sender, message):
        receiver = Device.objects(device_id=sender.receiver_id).first()
        receiver.update(add_to_set__messages=[message])

    @staticmethod
    def get_device_by_device_id(device_id):
        """
        Get the device by the device_id from the database or return None if it doesn't exist

        :param device_id:
        :return:
        """
        return Device.objects(device_id=device_id).first()