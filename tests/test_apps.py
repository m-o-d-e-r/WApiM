import unittest
import requests




class TestAppsAccess(unittest.TestCase):
    def setUp(self):
        random_app_payload = {
            "from_": 0,
            "to_": 0,
            "range_len": 0,
            "sorted_": True
        }

        self.__urls_d = [
            (
                "http://127.0.0.1:8000/random/int",
                random_app_payload
            ),
            (
                "http://127.0.0.1:8000/random/float",
                random_app_payload
            ),
            (
                "http://127.0.0.1:8000/random/weather_number",
                {
                    "count_weather_items": 0,
                    "temperature": True,
                    "humidity": True,
                    "wind_data": True,
                    "operation": "string"
                }
            ),
            (
                "http://127.0.0.1:8000/weather/at",
                {
                    "city": "string",
                    "temperature": True,
                    "humidity": True,
                    "wind_data": True
                }
            ),
            (
                "http://127.0.0.1:8000/weather/random_cords",
                {
                    "data_set_len": 0
                }
            )
        ]

    def test_app_access(self):
        for urld in self.__urls_d:
            self.assertEqual(
                requests.post(
                    urld[0],
                    json=urld[1]
                ).status_code,
                200
            )

    def test_error_responses(self):
        response: dict = None
        for urld in self.__urls_d:
            response = requests.post(
                urld[0],
                json=urld[1]
            ).json()
            self.assertNotEqual(response.get("info"), None)
            self.assertNotEqual(response.get("data"), None)
