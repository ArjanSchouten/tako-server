import flask
from flask_restful import Resource


class UpdateRequest(Resource):
    def get(self, version):
        response = flask.make_response()
        response.headers['Content-Type'] = 'application/octet-stream'
        #response.headers['x-MD5'] = 'this is a hash'
        f = open('./firmwareupdate-' + version + '.bin', 'r')
        response.data = f.readlines()
        f.close()
        return response
