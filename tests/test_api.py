from pytest import mark
from api_sample import call_api


@mark.smoke
class FirstEndpointTests:

    @mark.positive
    def test_positive_data(self, get_positive_api_data_1):
        result = call_api(*get_positive_api_data_1)
        status = result.status_code
        message = result.json()
        assert status == 200 and message['message'] == 'success'

    @mark.negative
    def test_negative_data(self, get_negative_api_data_1):
        result = call_api(*get_negative_api_data_1)
        status = result.status_code // 100
        assert status == 4


@mark.smoke
class SecondEndpointTests:

    @mark.positive
    def test_positive_data(self, get_positive_api_data_2):
        result = call_api(*get_positive_api_data_2)
        status = result.status_code
        message = result.json()
        assert status == 200 and message['message'] == 'success'

    @mark.negative
    def test_negative_data(self, get_negative_api_data_2):
        result = call_api(*get_negative_api_data_2)
        status = result.status_code // 100
        assert status == 4

