import hashlib
import os

import flask
from flask_restful import Resource, abort
from utils import firmwareupdate_filename, firmware_version_exists, firmwareupdate_path


class UpdateRequest(Resource):
    def get(self, version):
        filename = firmwareupdate_filename(version)

        if firmware_version_exists(filename) is False:
            abort(404)

        response = flask.make_response()
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['Content-Disposition'] = 'attachment; filename=\'' + filename + '\''

        f = open(firmwareupdate_path(version), 'r')
        hash_md5 = hashlib.md5()
        response.data = f.read()
        hash_md5.update(response.data)
        response.headers['x-MD5'] = hash_md5.hexdigest()
        f.close()
        return response
