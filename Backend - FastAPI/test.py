import unittest
from fastapi.testclient import TestClient
from app import app
import boto3

class TestAPI(unittest.TestCase):
    client = TestClient(app)
    data = {'age':30,
            "job":"services",
            "marital":"married",
            "education":"tertiary",
            "default":"no",
            "balance":1350,
            "housing":"yes",
            "loan":"no",
            "contact":"cellular",
            "day":16,
            "month":"oct",
            "duration":185,
            "campaign":1,
            "pdays":330,
            "previous":1,
            "poutcome":"other"}
    
    def test_reponse(self):
        """
        Vérifie que la reponse est correcte
        """
        reponse=self.client.post("/predict",
                     json=self.data)
        self.assertEqual(reponse.status_code,200)
        self.assertEqual(dict,type(reponse.json()))

# def test_error(self):
#     reponse=self.client.post("/predict",
#                 json="bonjour")
#     self.assertEqual(reponse.json()['msg'],'Input should be a valid dictionary or object to extract fields from')

        