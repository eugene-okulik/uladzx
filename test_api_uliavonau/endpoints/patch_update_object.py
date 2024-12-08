import requests
import allure

from endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):

    @allure.step('Update the object using PATCH method')
    def patch_edit_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
