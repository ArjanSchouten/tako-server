from flask import Flask
from flask_restful import Api
from pingrequest import PingRequest


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def run(self):
        self.register_routes()
        self.app.run(debug=False, host='0.0.0.0', port=8888)
        return self.app

    def register_routes(self):
        # Route definitions
        self.api.add_resource(PingRequest, '/ping')


if __name__ == '__main__':
    app = App()
    app.run()
