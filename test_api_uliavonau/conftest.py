import pytest
import requests
import allure

from endpoints.create_object import CreateObject
from endpoints.put_update_object import UpdateObjectPut
from endpoints.patch_update_object import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def put_update_object_endpoint():
    return UpdateObjectPut()


@pytest.fixture()
def patch_update_object_endpoint():
    return UpdateObjectPatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_and_delete_new_object():
    body = {
        "name": "10.10.2024 object",
        "data": {"color": "red", "size": "large", "userId": 1}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
