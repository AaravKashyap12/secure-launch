import unittest
from fastapi.testclient import TestClient
from app import app
class Health(unittest.TestCase):
    def test_health(self):self.assertEqual(TestClient(app).get('/health').status_code,200)
if __name__=='__main__':unittest.main()
