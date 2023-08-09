import time
import unittest
import requests
import subprocess

BASE_URL = "http://localhost:5000"


class ApiHealthTest(unittest.TestCase):

    proc = None

    @classmethod
    def setUpClass(cls):
        cls.proc = subprocess.Popen(["flask", "--app", "../simple_railcontroller/rest_controller", "run"])
        time.sleep(2)
        print("start")

    @classmethod
    def tearDownClass(cls):
        cls.proc.kill()
        print("stop")

    def test_health_ok(self):
        expected = "hello world"
        actual = requests.get(f'{BASE_URL}/health').content.decode("utf-8")
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
