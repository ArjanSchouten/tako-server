import json

from mongoengine import connect

from models.device import Device
from models.message import Message
from util import BaseTest


class PingRequestTest(BaseTest):
    def test_header_existence(self):
        response = self.client.get("/ping")
        self.assert400(response)

        response = self.client.get("/ping", headers={'Device-ID': 'ABC'})
        self.assert400(response)

        response = self.client.get("/ping", headers={'Firmware-Version': '1.0.0'})
        self.assert400(response)

    def test_device_not_found(self):
        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': 'ABC'})
        self.assert404(response)

        device = Device(device_id='ABC', receiver_id='CBA').save()
        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': device.device_id})
        self.assert200(response)
        try:
            data = json.loads(response.data)
            self.assertEqual(len(data['messages']), 0)
        except ValueError:
            self.assertTrue(False, "The ping request didn't return json")

        device.messages = [Message(message='This is a test')]
        device.save()

        response = self.client.get('/ping', headers={'Firmware-Version': '1.0.0', 'Device-ID': device.device_id})
        self.assert200(response)
        try:
            data = json.loads(response.data)
            self.assertEqual(len(data['messages']), 1)
        except ValueError:
            self.assertTrue(False, "The ping request didn't return json")


