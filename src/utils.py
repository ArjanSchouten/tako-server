import os
from functools import wraps

import flask
from flask_restful import abort

storage = '/var/www/firmwarestore/'


def check_firmware_version_header(func):
    """
    Decorator which checks if the Firmware-Version of the ESP8266 is set in the HTTP request.

    Example:
    ```
    @check_firmware_version_header
    def get(self):
        pass
    ```

    :param func:
    :return:
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):
        version = flask.request.headers.get('Firmware-Version')
        if version is None:
            return abort(400)
        kwargs['firmware_version'] = version
        return func(*args, **kwargs)

    return decorated_function


def check_device_id_header(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        device_id = flask.request.headers.get('Device-ID')

        if device_id is None:
            return abort(400)

        kwargs['device_id'] = device_id

        return func(*args, **kwargs)

    return decorated_function


def firmwareupdate_path(version):
    return storage + firmwareupdate_filename(version)


def firmwareupdate_filename(version):
    return 'firmwareupdate-%d.bin'.format(version)


def firmware_version_exists(filename):
    return os.path.isfile(storage + filename)
