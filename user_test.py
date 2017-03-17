import urllib
from flask_testing import TestCase
from flask import Flask
import unittest
from main import app

class UserTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_assert_not_process_the_template(self):
        response = self.client.get("/")
        print(response.data)
        assert response.data == 'this will be the start page'

if __name__ == '__main__':
    unittest.main()
