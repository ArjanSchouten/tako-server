import json

from models.device import Device
from util import BaseTest


class SendMessageRequestTest(BaseTest):
    def test_header_existence(self):
        response = self.client.get("/send")
        self.assert405(response)

        response = self.client.post("/send")
        self.assert400(response)

        response = self.client.post("/send", headers={'Device-ID': 'ABC'})
        self.assert400(response)

    def test_send_message(self):
        headers = {'Device-ID': 'BLABLA'}
        # Without sending the data we expect a BadRequest response
        response = self.client.post("/send", headers=headers)
        self.assert400(response)

        # Since the device isn't in the database we expect a 404
        headers['Content-Type'] = 'application/json'
        response = self.client.post("/send",
                                    headers=headers,
                                    data='{"message": "test"}')
        self.assert404(response)

        Device(device_id=headers['Device-ID'], receiver_id='TEST').save()
        Device(device_id='TEST', receiver_id=headers['Device-ID']).save()
        response = self.client.post("/send",
                                    headers=headers,
                                    data='{"message": "test"}')
        self.assert200(response)
        inserted_message = Device.objects(device_id='TEST').first().messages[0]
        self.assertIsNotNone(inserted_message)
        self.assertEqual(inserted_message.message, 'test')

        headers.pop('Content-Type', None)
        response = self.client.get('/ping', headers={'Firmware-Version': '1', 'Device-ID': 'TEST'})
        self.assert200(response)
        try:
            data = json.loads(response.data)
            self.assertEqual(data['message'], 'test')
        except ValueError:
            self.assertTrue(False, 'No json is returned from the ping request')
