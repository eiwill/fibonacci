import unittest
import requests


class FunctionalTestCase(unittest.TestCase):

    def test_simple_flow(self):
        """
        Get sequence from server and validate it
        """
        res = self.make_request("GET", "/fibonacci/%s" % 10)
        self.assertEqual(res.status_code, 200)
        data = res.json()

        self.assertListEqual(data, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

        self.assertEqual(res.headers["Content-Type"], "application/json")

    def make_request(self, method, uri, **kwargs):
        return requests.request(method, "http://localhost:8081%s" % uri, **kwargs)
