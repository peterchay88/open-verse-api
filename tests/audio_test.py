import pytest
import logging as logger
from tests.conftest import v2_header
from src.utils.api_endpoints.audio_endpoint import AudioEndpoint

pytestmark = [pytest.mark.audio]


class TestAudio:

    @pytest.mark.parametrize("query_param", [
        # pytest.param("", marks=pytest.mark.audio_no_params),
        pytest.param("test", marks=pytest.mark.audio_test),
        pytest.param("dog+cat", marks=pytest.mark.audio_dog_and_cat),
        pytest.param("Giacomo Puccini", marks=pytest.mark.giacomo_puccini),
    ])
    def test_audio_OVA_T1(self, query_param, page, page_size, v2_header):
        """
        This test confirms we receive the expected response when
        hitting the audio endpoint with the supplied parameters
        :return:
        """
        params = {
            "q": query_param,
            "page": page,
            "page_size": page_size
        }
        logger.info("Running audio tests")
        audio = AudioEndpoint()
        result = audio.get_audio_search(token_header=v2_header, params=params)
        logger.info("%s", result['result_count'])
        # logger.info(result)
        for key, value in result['results'][0].items():
            pass # TODO: Work on assertion method. Going to figure out Zephyr integration first


