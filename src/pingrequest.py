from flask_restful import Resource
from flask import request


class PingRequest(Resource):
    # Handle the post request
    def get(self):
        #deviceid = request.headers.get('deviceID')

        return {'update': False, 'messages': []}
