from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Ping(Resource):
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

# Route definitions
api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    app.run(debug=True)
