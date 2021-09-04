import unittest

from app import app


class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_response_of_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.data.decode("utf-8"), "Hello World!")
        

if __name__ == "__main__":
    unittest.main()
