import unittest
from fastapi.testclient import TestClient
from app import IDENTITIES, app


def fixture_identity(tenant):
    return next(value for value,subject in IDENTITIES.items() if subject['tenant']==tenant)


class Health(unittest.TestCase):
    def setUp(self):self.client=TestClient(app)

    def test_health(self):self.assertEqual(self.client.get('/health').status_code,200)

    def test_baseline_headers(self):
        response=self.client.get('/health')
        self.assertEqual(response.headers['x-content-type-options'],'nosniff')
        self.assertEqual(response.headers['x-frame-options'],'DENY')
        self.assertEqual(response.headers['referrer-policy'],'no-referrer')

    def test_same_tenant_record_access(self):
        response=self.client.get('/records/a-note',headers={'authorization':fixture_identity('a')})
        self.assertEqual(response.status_code,200)

    def test_cross_tenant_record_access_is_denied(self):
        response=self.client.get('/records/b-note',headers={'authorization':fixture_identity('a')})
        self.assertEqual(response.status_code,403)
if __name__=='__main__':unittest.main()
