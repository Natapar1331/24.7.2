from api import PetFriends
from settings import valid_email, valid_password


 pf = PetFriends()


 def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
     status, result = pf.get_api_key_(email, password)
     assert status == 200
     assert `key` in result

     def test_get_all_pets_with_valid_key(filter=``):
         _, auth_key = pf.get_api_key(valid_email, valid_password)
         status, result = pf.get_list_of_pets(auth_key, filter)
         assert status== 200
         assert len(result[`pets`]) > 0

import unittest
import requests
from api import PetFriendsAPI

class TestPetFriendsAPI(unittest.TestCase):
    def setUp(self):
        self.api = PetFriendsAPI()
        self.api.auth_key = "valid_auth_key"

    def test_get_pet_valid(self):
        response = self.api.get_pet("1")
        self.assertEqual(response['status'], 'success')

    def test_get_pet_invalid(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.get_pet("999999")

    def test_add_pet_valid(self):
        data = {
            "name": "Бобик",
            "animal_type": "Собака",
            "age": 5,
            "breed": "Бородатая"
        }
        response = self.api.add_pet(data)
        self.assertEqual(response['status'], 'success')

    def test_add_pet_missing_data(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.add_pet({})

    def test_add_pet_invalid_key(self):
        self.api.auth_key = "invalid_auth_key"
        data = {
            "name": "Бобик",
            "animal_type": "Собака",
            "age": 5,
            "breed": "Бородатая"
        }
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.add_pet(data)

    def test_edit_pet_valid(self):
        data = {
            "name": "Шарик",
            "animal_type": "Собака",
            "age": 6,
            "breed": "Лабрадор"
        }
        response = self.api.edit_pet("1", data)
        self.assertEqual(response['status'], 'success')

    def test_edit_pet_invalid_key(self):
        self.api.auth_key = "invalid_auth_key"
        data = {
            "name": "Шарик",
            "animal_type": "Собака",
            "age": 6,
            "breed": "Лабрадор"
        }
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.edit_pet("1", data)

    def test_edit_pet_invalid_id(self):
        data = {
            "name": "Шарик",
            "animal_type": "Собака",
            "age": 6,
            "breed": "Лабрадор"
        }
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.edit_pet("999999", data)

    def test_delete_pet_valid(self):
        response = self.api.delete_pet("1")
        self.assertEqual(response['status'], 'success')

    def test_delete_pet_invalid_key(self):
        self.api.auth_key = "invalid_auth_key"
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.delete_pet("1")

    def test_delete_pet_invalid_id(self):
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.delete_pet("999999")

    def test_add_pet_large_values(self):
        data = {
            "name": "Бобик" * 1000,
            "animal_type": "Собака",
            "age": 5,
            "breed": "Бородатая"
        }
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.add_pet(data)

    def test_add_pet_missing_key(self):
        self.api.auth_key = None
        data = {
            "name": "Бобик",
            "animal_type": "Собака",
            "age": 5,
            "breed": "Бородатая"
        }
        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.add_pet(data)

if __name__ == '__main__':
    unittest.main()