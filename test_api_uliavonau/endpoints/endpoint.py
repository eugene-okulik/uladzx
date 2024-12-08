import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    response_json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that response is 200')
    def check_response_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_updated(self, name):
        assert self.response_json['name'] == name

    @allure.step('Check that data is updated')
    def check_response_data_is_updated(self, data):
        assert self.response_json['data'] == data
