import json

from flask_testing import TestCase
from mongoengine import connect

from models.device import Device
from models.message import Message
from src.takoapp import TakoApp


class PingRequestTest(TestCase):
    def create_app(self):
        # Create an app without spawning a real server so we can execute fake requests
        app = TakoApp()
        app.register_routes()
        app.app.config['TESTING'] = True
        return app.app

    def test_header_existence(self):
        response = self.client.get("/ping")
        self.assert400(response)

        response = self.client.get("/ping", headers={'Device-ID': 'ABC'})
        self.assert400(response)

        response = self.client.get("/ping", headers={'Firmware-Version': '1.0.0'})
        self.assert400(response)

    def test_device_not_found(self):
        connect('mongoenginetest', host='mongomock://localhost')
        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': 'ABC'})
        self.assert404(response)

        device = Device(device_id='ABC', receiver_id='CBA').save()
        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': device.device_id})
        self.assert200(response)
        try:
            data = json.loads(response.data)
            self.assertEqual(len(data['messages']), 0)
        except:
            self.assertTrue(False, "The ping request didn't return json")

        device.messages = [Message(message='This is a test')]
        device.save()

        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': device.device_id})
        self.assert200(response)
        try:
            data = json.loads(response.data)
            self.assertEqual(len(data['messages']), 1)
        except:
            self.assertTrue(False, "The ping request didn't return json")


