import pytest
import logging as logger
from tests.conftest import v2_header
from src.utils.requests.audio_endpoint import AudioEndpoint

pytestmark = [pytest.mark.audio]


class TestAudio:

    @pytest.mark.parametrize("query_param", [
        # pytest.param("", marks=pytest.mark.audio_no_params),
        pytest.param("test", marks=pytest.mark.audio_test),
        pytest.param("dog+cat", marks=pytest.mark.audio_dog_and_cat),
        pytest.param("%22Giacomo%20Puccini%22", marks=pytest.mark.exact_match),
    ])
    def test_audio_OVA_T1(self, query_param, v2_header):
        """
        This test confirms we receive the expected response when
        hitting the audio endpoint with the supplied parameters
        :return:
        """
        logger.info("Running audio tests")
        audio = AudioEndpoint()
        result = audio.get_audio_search(token_header=v2_header, params=query_param)
        logger.info("%s", result['result_count'])
        # logger.info(result)
        # TODO: Figure out how we assert what we return
