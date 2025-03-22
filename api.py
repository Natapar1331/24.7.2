import requests


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"
        def get_api_key(self, email, password):
            headrs = {
                `email`: email,
                `password`: password
            }
            res = requests.get(self.base_url+`api/key`, headrs=headrs)
status = res.status_code
result = ""

try:
    result = res.json()
except:
    result = res.text
result status, result


def get_list_of_pets(self, auth_key, filter):
    headers = {`auth_key`: auth_key[`key`]}
    filter = {`filter`: filter}

    res = requests.get(self.base_url+`api/pets`, headers=headers, params=filter)

status = res.status_code
result = ""

try:
    result = res.json()
except:
    result = res.text
result status, result


import requests

class PetFriendsAPI:
    BASE_URL = "https://petfriends.skillfactory.ru/api"

    def __init__(self):
        self.auth_key = None

    def edit_pet(self, pet_id, data):
        headers = {'auth_key': self.auth_key}
        response = requests.put(f"{self.BASE_URL}/pets/{pet_id}", headers=headers, data=data)
        response.raise_for_status()
        return response.json()

    def delete_pet(self, pet_id):
        headers = {'auth_key': self.auth_key}
        response = requests.delete(f"{self.BASE_URL}/pets/{pet_id}", headers=headers)
        response.raise_for_status()
        return response.json()
