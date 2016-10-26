from flask import Flask
from flask import make_response
from flask_restful import output_json
from flask_restful import Api
from models.device import Device
from mongoengine import connect

from ping_request import PingRequest
from send_message import SendMessageRequest
from update_request import UpdateRequest


class TakoApp:
    """
    TakoApp which makes it easier to run the tests without spawning a real server.
    """

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def run(self):
        self.register_routes()
        self.database_connect()
        # Fake data because of quick prototype :)
        Device(device_id="test1234", receiver_id="test").save()
        Device(device_id="test", receiver_id="test1234").save()
        self.app.run(debug=True, host='0.0.0.0', port=8888)
        return self.app

    def register_routes(self):
        # Register the route definitions
        self.api.add_resource(PingRequest, '/ping')
        self.api.add_resource(SendMessageRequest, '/send')
        self.api.add_resource(UpdateRequest, '/update/<string:version>')

    @staticmethod
    def database_connect():
        connect('tako', host='db', port=27017, username='tako', password='password')


if __name__ == '__main__':
    flaskApp = TakoApp()


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

