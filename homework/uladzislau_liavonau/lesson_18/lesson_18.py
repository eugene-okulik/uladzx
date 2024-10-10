import requests


def new_post():
    body = {
        "name": "10.10.2024 object",
        "data": {
            "color": "red",
            "size": "large",
            "userId": 1
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    return response.json()['id']


def clear(post_id):
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


def get_post_by_id(post_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, 'Object not found'
    return response.json()


def post_a_post():
    post_id = new_post()
    created_object = get_post_by_id(post_id)
    assert created_object['name'] == "10.10.2024 object", 'Object name is incorrect'
    clear(post_id)


def put_a_post():
    post_id = new_post()
    body = {
        "name": "10.10.2024 object_UPD",
        "data": {
            "color": "blue",
            "size": "large",
            "userId": 1
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['color'] == "blue", 'Value does not match'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "name": "10.10.2024 object_UPD_by_patch_method",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == '10.10.2024 object_UPD_by_patch_method'
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


post_a_post()
put_a_post()
patch_a_post()
delete_a_post()
