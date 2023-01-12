import requests


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }

        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_pet_simple(self, auth_key, name, animal_type, age):
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}

        res = requests.post(self.base_url + 'api/create_pet_simple', data=data, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_new_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo):
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        files = {'pet_photo': pet_photo}
        res = requests.post(self.base_url + 'api/pets', data=data, files=files, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def create_new_pet_id_set_photo(self, auth_key, pet_id, pet_photo):
        headers = {'auth_key': auth_key['key']}
        data = {'pet_id': pet_id}
        files = {'pet_photo': pet_photo}
        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, data=data, files=files, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def put_pet(self, auth_key, pet_id, name=None, animal_type=None, age=None):
        headers = {'auth_key': auth_key['key']}
        data = {'pet_id': pet_id, 'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.put(self.base_url + '/api/pets/' + pet_id, data=data, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url +'/api/pets/' + pet_id, headers=headers)
        status = res.status_code

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

