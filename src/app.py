from flask import Flask
from flask import make_response
from flask.ext.restful import output_json
from flask_restful import Api
from mongoengine import connect

from ping_request import PingRequest


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def run(self):
        connect('tako', host='db', port=27017, username='tako', password='password')
        self.register_routes()
        self.app.run(debug=True, host='0.0.0.0', port=8888)
        return self.app

    def register_routes(self):
        # Route definitions
        self.api.add_resource(PingRequest, '/ping')


if __name__ == '__main__':
    flaskApp = App()


    @flaskApp.api.representation('application/json')
    def json(data, code, headers):
        """
        Flask will output an error message in json format by default.
        To prevent that we leak important information remove all messages from non 200 responses
        """
        if code == 200:
            return output_json(data, code, headers)
        else:
            return make_response('', code, headers)


    flaskApp.run()
