import pytest


TEST_DATA = [
    {
        "name": "Object 1",
        "data": {
            "color": "red",
            "size": "small",
            "userId": 1,
        },
    },
    {
        "name": "Object 2",
        "data": {
            "color": "blue",
            "size": "medium",
            "userId": 2,
        },
    },
    {
        "name": "Object 3",
        "data": {
            "color": "green",
            "size": "large",
            "userId": 3,
        },
    },
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_an_object(
        create_object_endpoint,
        delete_object_endpoint,
        data
):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_response_status_is_200()
    object_id = create_object_endpoint.object_id

    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_response_status_is_200()


def test_update_object_using_put(
        create_and_delete_new_object,
        put_update_object_endpoint
):
    print(f"New object id is {create_and_delete_new_object}")

    updated_data = {
        "name": "10.10.2024 object__UPD_using_PUT",
        "data": {"color": "blue", "size": "small", "userId": 1}
    }

    (put_update_object_endpoint.put_edit_object
     (create_and_delete_new_object, updated_data).json())
    put_update_object_endpoint.check_response_status_is_200()
    (put_update_object_endpoint.check_response_name_is_updated
     (updated_data['name']))


def test_update_object_using_patch(
        create_and_delete_new_object,
        patch_update_object_endpoint
):
    print(f"New object id is {create_and_delete_new_object}")

    updated_data = {"name": "10.10.2024 object_UPD_using_PATCH"}

    (patch_update_object_endpoint.patch_edit_object
     (create_and_delete_new_object, updated_data).json())
    patch_update_object_endpoint.check_response_status_is_200()
    (patch_update_object_endpoint.check_response_name_is_updated
     (updated_data['name']))


def test_delete_created_object(create_and_delete_new_object, delete_object_endpoint):
    delete_object_endpoint.delete_object(create_and_delete_new_object)
    delete_object_endpoint.check_response_status_is_200()
    print(f"Object is deleted")

