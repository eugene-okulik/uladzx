import requests
import allure

from uladzx.test_api_uliavonau.endpoints.endpoint import Endpoint


class UpdateObjectPut(Endpoint):

    @allure.step('Update the object using PUT method')
    def put_edit_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
