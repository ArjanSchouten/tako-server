from flask import Flask, request
from flask_restful import Resource, Api
from pingrequest import PingRequest

app = Flask(__name__)
api = Api(app)

# Route definitions
api.add_resource(PingRequest, '/ping')

if __name__ == '__main__':
    app.run(debug=True)
