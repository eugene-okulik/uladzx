import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {"name": "10.10.2024 object", "data": {"color": "red", "size": "large", "userId": 1}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(f'\nCreated post ID: {post_id}')
    yield post_id
    print(f'\nDeleted post ID: {post_id}')
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


@pytest.fixture(scope='session')
def start_and_completed_testing():
    print('\n\nStart testing')
    yield
    print('\nTesting completed')


@pytest.mark.critical
@pytest.mark.parametrize(
    "body",
    [
        {"name": "Object 1", "data": {"color": "red", "size": "small", "userId": 1}},
        {"name": "Object 2", "data": {"color": "blue", "size": "medium", "userId": 2}},
        {"name": "Object 3", "data": {"color": "green", "size": "large", "userId": 3}},
    ]
)
def test_post_a_post(body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )

    assert response.status_code == 200, 'Status code is incorrect'
    post_id = response.json()['id']
    print(f"Created object with ID: {post_id} and data: {body}")

    get_response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')
    assert get_response.status_code == 200, 'Object not found'
    get_data = get_response.json()
    assert get_data['id'] == post_id, 'Returned ID does not match created object ID'
    assert get_data['name'] == body['name'], 'Name does not match'
    assert get_data['data'] == body['data'], 'Data does not match'

    delete_response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert delete_response.status_code == 200, 'Failed to delete created object'
    print(f"Deleted object with ID: {post_id}")


def test_put_a_post(new_post_id):
    print('before test')
    body = {"name": "10.10.2024 object_UPD", "data": {"color": "blue", "size": "large", "userId": 1}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body,
        headers=headers
    ).json()

    assert response['data']['color'] == "blue", 'Value does not match'
    print('after test')


@pytest.mark.medium
def test_patch_a_post(new_post_id):
    print('before test')
    body = {"name": "10.10.2024 object_UPD_by_patch_method", }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_post_id}',
        json=body,
        headers=headers
    ).json()

    assert response['name'] == '10.10.2024 object_UPD_by_patch_method', 'Name does not match'
    print('after test')


def test_delete_a_post(new_post_id):
    print('before test')
    requests.delete(f'http://167.172.172.115:52353/object/{new_post_id}')
    print('after test')
