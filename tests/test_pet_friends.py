from api import PetFriends
from settings import valid_email, valid_password


class TestPetFriends:
    def setup(self):
        self.pf = PetFriends()

    def test_get_api_key_for_valid_user(self):
        status, result = self.pf.get_api_key(valid_email, valid_password)
        assert status == 200
        assert 'key' in result

    def test_get_all_pets_with_valid_key(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        status, result = self.pf.get_list_of_pets(auth_key, '')
        assert status == 200
        assert len(result['pets']) > 0

    def test_create_pet_simple(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        name = 'Барсик'
        type = 'кот'
        age = '5'

        status, result = self.pf.create_pet_simple(auth_key, name, type, age)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == type
        assert result['age'] == age

    def test_create_pet_simple_bad_params(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        name = ''
        type = ''
        age = ''

        status, result = self.pf.create_pet_simple(auth_key, name, type, age)

        assert status == 400

    def test_create_pet_simple_bad_key(self):
        auth_key = {'key': 'bad_key'}
        name = 'Барсик'
        type = 'кот'
        age = '5'

        status, result = self.pf.create_pet_simple(auth_key, name, type, age)

        assert status == 403

    def test_create_new_pet_with_photo(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        name = 'Изя'
        type = 'кот'
        age = '4'
        foto = open('./images/cat.jpg', 'rb')

        status, result = self.pf.create_new_pet_with_photo(auth_key, name, type, age, foto)

        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == type
        assert result['age'] == age
        assert result['pet_photo'] != ''

    def test_create_new_pet_id_set_photo(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        name = 'Петр'
        type = 'кот'
        age = '4'
        _, pet = self.pf.create_pet_simple(auth_key, name, type, age)
        pet_id = pet['id']
        foto = open('./images/cashak.jpg', 'rb')

        status, result = self.pf.create_new_pet_id_set_photo(auth_key, pet_id, foto)

        assert status == 200
        assert result['pet_photo'] != ''

    def test_set_photo_unknown_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        pet_id = ''
        foto = open('./images/cat.jpg', 'rb')

        status, result = self.pf.create_new_pet_id_set_photo(auth_key, pet_id, foto)
        assert status == 404

    def test_put_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        _, pet = self.pf.create_pet_simple(auth_key, 'Изя', 'dog', 6)
        pet_id = pet['id']

        status, result = self.pf.put_pet(auth_key, pet_id, 'Vesha', 'кошак', 5)

        assert status == 200
        assert result['age'] == '5'
        assert result['name'] == 'Vesha'
        assert result['animal_type'] == 'кошак'

    def test_put_pet_bad_params(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        pet_id = ''

        status, result = self.pf.put_pet(auth_key, pet_id, 'Вульф')
        assert status == 404

    def test_del_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        name = 'Петр'
        type = 'кот'
        age = '4'
        _, pet = self.pf.create_pet_simple(auth_key, name, type, age)
        pet_id = pet['id']

        status, _ = self.pf.delete_pet(auth_key, pet_id)

        assert status == 200

    def test_del_unknown_pet(self):
        _, auth_key = self.pf.get_api_key(valid_email, valid_password)
        pet_id = ''

        status, _ = self.pf.put_pet(auth_key, pet_id)
        assert status == 404
