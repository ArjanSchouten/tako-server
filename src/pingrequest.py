from flask_restful import Resource
from flask import request, abort


class PingRequest(Resource):
    # Handle the post request
    def get(self):
        deviceid = request.headers.get('deviceID')
        version = request.headers.get('firmware_version')

        if deviceid is None or version is None:
            abort(400)

        return {'update': False, 'messages': []}
