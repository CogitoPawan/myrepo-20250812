import unittest
from anomaly_detector.server import app

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_anomalies_endpoint(self):
        response = self.app.get('/anomalies')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()