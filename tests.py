import unittest

from app import app


class BaseUnitTests(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self) -> None:
        pass


class HelloWorldTests(BaseUnitTests):

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_response_of_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.data.decode("utf-8"), "Hello World!")


class WeatherTests(BaseUnitTests):

    def test_weather_endpoint(self):
        query_string = {"lat": "12", "lon": "-23"}
        response = self.app.get('/weather', data=query_string, follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
