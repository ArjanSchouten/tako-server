from flask_restful import Resource, abort

from utils import check_firmware_version_header, check_device_id_header


class SendMessageRequest(Resource):
    @check_firmware_version_header
    @check_device_id_header
    def get(self, firmware_version, device_id):
        abort(400)
