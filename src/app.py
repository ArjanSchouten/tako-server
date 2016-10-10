from flask import Flask
from flask_restful import Api
from pingrequest import PingRequest

app = Flask(__name__)
api = Api(app)

# Route definitions
api.add_resource(PingRequest, '/ping')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888)
