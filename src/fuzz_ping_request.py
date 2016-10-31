import flask
import fuzzing
from flask_restful import Resource

seed = "{\"message\": \"test\", \"newversion\": \"5\", \"update\": false}"
number_of_fuzzed_variants_to_generate = 1000
fuzz_factor = 50
fuzzed_data = fuzzing.fuzz_string(seed, number_of_fuzzed_variants_to_generate, fuzz_factor)
current_fuzz = 0
print(fuzzed_data)


class FuzzPingRequest(Resource):
    def get(self):
        global current_fuzz
        current_fuzz += 1
        response = flask.make_response()
        response.data = fuzzed_data[current_fuzz % number_of_fuzzed_variants_to_generate]

        return response
