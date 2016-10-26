import hashlib
import os

import flask
from flask_restful import Resource, abort


class UpdateRequest(Resource):
    storage = '/var/www/firmwarestore/'
    def get(self, version):
        response = flask.make_response()
        response.headers['Content-Type'] = 'application/octet-stream'
        file = 'firmwareupdate-' + version + '.bin'
        response.headers['Content-Disposition'] = 'attachment; filename=\'+file'+'\''
        if os.path.isfile(self.storage + file) is False:
            abort(404)

        f = open('./firmwareupdate-' + version + '.bin', 'r')
        hash_md5 = hashlib.md5()
        response.data = f.read()
        hash_md5.update(response.data)
        response.headers['x-MD5'] = hash_md5.hexdigest()
        f.close()
        return response
