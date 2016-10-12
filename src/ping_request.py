from flask_restful import Resource, abort
from flask import request, jsonify

from models.device import Device


class PingRequest(Resource):
    def get(self):
        """
        Handle the GET request comming from the ESP8266.
        The Firmware-Version and the Device-ID should be passed in the headers.

        :return:
        """
        device_id = request.headers.get('Device-ID')
        version = request.headers.get('Firmware-Version')

        if device_id is None or version is None:
            abort(400)

        # Lookup the device in the database or abort if it isn't found
        device = self.get_device_by_device_id(device_id)
        if device is None:
            abort(404)

        return {'update': False, 'messages': map(lambda m: m.message, device.messages)}

    @staticmethod
    def get_device_by_device_id(device_id):
        """
        Get the device by the device_id from the database or return None if it doesn't exist

        :param device_id:
        :return:
        """
        return Device.objects(device_id=device_id).first()
