from main import app
from flask import json
import unittest

class testCase_1(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        response = app.test_client().post(
            '/generate-token',
            data=json.dumps({"id":"MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"}),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data["signature"] == '89936954ea2bbbc1332cadbb9668c01b0b4faee728c0345ff1259c74dfb312f8'
    
    def tearDown(self):
        pass

class testCase_2(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        response = app.test_client().post(
            '/generate-token',
            data=json.dumps({"message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."}),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data["signature"] == '7e2c942d3a4b7c361242ceb191ab83fcea638d3190b6a3fef40b4324699d4de6'
    
    def tearDown(self):
        pass
        


class twiceValid(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        payload1 = {"message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."}
        payload2 = payload1
        response = app.test_client().post(
            '/generate-token',
            data=json.dumps(payload1),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data["signature"] == '7e2c942d3a4b7c361242ceb191ab83fcea638d3190b6a3fef40b4324699d4de6'

        # Verify that same object returns same result
        response = app.test_client().post(
            '/generate-token',
            data=json.dumps(payload2),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data["signature"] == '7e2c942d3a4b7c361242ceb191ab83fcea638d3190b6a3fef40b4324699d4de6'
    
    def tearDown(self):
        pass


class complexValid(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        payload = {"id" :"MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz",
            "message": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey."}
        response = app.test_client().post(
            '/generate-token',
            data=json.dumps(payload),
            content_type='application/json',
        )
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data["signature"] == '9e6b4837b15345fa64f38ea92286a8068c2911e7d2fd45ec7fff5618fea2be8c'

    def tearDown(self):
        pass


class invalidJsonString(unittest.TestCase):
    def setUp(self):
        pass

    def test(self):
        response = app.test_client().post(
            '/generate-token',
            data="This is just a string",
            content_type='application/json',
        )
        print(response)
        assert response.status_code == 400
    
    def tearDown(self):
        pass

