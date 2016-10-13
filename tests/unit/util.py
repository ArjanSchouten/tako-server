from flask_testing import TestCase
from mongoengine import connect

from takoapp import TakoApp


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost')

    def create_app(self):
        # Create an app without spawning a real server so we can execute fake requests
        app = TakoApp()
        app.register_routes()
        app.app.config['TESTING'] = True
        return app.app
