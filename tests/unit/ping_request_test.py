from flask_testing import TestCase

from src.app import App


class PingRequestTest(TestCase):
    def create_app(self):
        app = App()
        app.register_routes()
        app.app.config['TESTING'] = True
        return app.app

    def test_require_device_id(self):
        response = self.client.get("/ping")
        self.assert400(response)

        response = self.client.get("/ping", headers={'deviceID': "ABC"})
        self.assert400(response)

        response = self.client.get("/ping", headers={'version': "1.0.0"})
        self.assert400(response)
