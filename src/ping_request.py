from flask_restful import Resource, abort

from models.device import Device
from utils import check_firmware_version_header, check_device_id_header


class PingRequest(Resource):
    @check_firmware_version_header
    @check_device_id_header
    def get(self, firmware_version, device_id):
        # Lookup the device in the database or abort if it isn't found
        device = self.get_device_by_device_id(device_id)
        if device is None:
            abort(404)

        if len(device.messages) > 0:
            return {'update': False, 'message': device.messages.pop().message}
        else:
            return {'update': False}

    @staticmethod
    def get_device_by_device_id(device_id):
        """
        Get the device by the device_id from the database or return None if it doesn't exist

        :param device_id:
        :return:
        """
        return Device.objects(device_id=device_id).first()
