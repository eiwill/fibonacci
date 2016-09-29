import json
import unittest

from fibonacci.frontend import app


class FrontendTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get_simple(self):
        """
        Check simple sequences
        """
        self.get_fibonacci(4, 200, [0, 1, 1, 2])

        self.get_fibonacci(0, 200, [])

    def test_get_negative_count(self):
        """
        Check "400" returned for negative number
        """
        self.get_fibonacci(-4, 400)

    def test_get_nonint_count(self):
        """
        Check "400" returned for not int
        """
        self.get_fibonacci("abcd123", 400)

    def test_get_exceed_limit_count(self):
        """
        Check "400" returned for exceed count
        """
        self.get_fibonacci(app.config["MAXIMUM_FIBONACCI_COUNT"] + 1, 400)

    def get_fibonacci(self, count, expected_code, expected_sequence=None):
        rv = self.app.get("/fibonacci/%s" % count)
        self.assertEqual(rv.status_code, expected_code)

        if expected_code != 200:
            return

        data = json.loads(rv.data)
        self.assertListEqual(data, expected_sequence)

        self.assertEqual(rv.headers['Content-Type'], "application/json")
