import pytest

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
