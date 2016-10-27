from flask_restful import Resource, abort

from models.device import Device
from utils import check_firmware_version_header, check_device_id_header, firmware_version_exists, \
    firmwareupdate_filename


class PingRequest(Resource):
    @check_firmware_version_header
    @check_device_id_header
    def get(self, firmware_version, device_id):
        newversion = int(firmware_version) + 1
        update = firmware_version_exists(firmwareupdate_filename(newversion))

        # Lookup the device in the database or abort if it isn't found
        device = self.get_device_by_device_id(device_id)
        if device is None:
            abort(404)

        if len(device.messages) > 0:
            return {'update': update, 'message': device.messages.pop().message}
        elif update:
            return {'update': update, 'newversion': '%d' % newversion}
        else:
            return {'update': update}

    @staticmethod
    def get_device_by_device_id(device_id):
        """
        Get the device by the device_id from the database or return None if it doesn't exist

        :param device_id:
        :return:
        """
        return Device.objects(device_id=device_id).first()
