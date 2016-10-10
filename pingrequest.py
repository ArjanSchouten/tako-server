from flask_restful import Resource
from flask import request


class PingRequest(Resource):
    # Handle the post request
    def post(self):
        # Validate the content type
        if request.content_type != 'application/json':
            pass
        if request.charset.lower() != 'utf-8':
            pass

        json = request.get_json(silent=True)
        if json is None:
            pass

        return {'update': False, 'messages': []}
