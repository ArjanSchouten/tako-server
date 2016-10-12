from flask_restful import Resource, abort
from flask import request, jsonify
from models.device import Device


class PingRequest(Resource):
    """
    Handle the ping request from the ESP8266 module and send back the required information
    """

    def get(self):
        device_id = request.headers.get('Device-ID')
        version = request.headers.get('Firmware-Version')

        if device_id is None or version is None:
            abort(400)

        device = self.get_device_by_device_id(device_id)
        if device is None:
            abort(404)

        return {'update': False, 'messages': map(lambda m: m.message, device.messages)}

    def get_device_by_device_id(self, device_id):
        return Device.objects(device_id=device_id).first()
