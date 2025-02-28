from src.utils.requests.base_requests import BaseRequests
import logging as logger


class AudioEndpoint(BaseRequests):

    def __init__(self):
        super().__init__()
        self.__audio_endpoint = "v1/audio/?q="

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    def url(self):
        return super().base_url() + self.audio_endpoint()

    def audio_endpoint(self):
        return self.__audio_endpoint

    # ------------------------------------------------------------------------
    # Methods for tests
    # ------------------------------------------------------------------------
    def get_audio_search(self, token_header: dict, params: str = None):
        """
        Hits the get audio endpoint
        :return:
        """
        logger.info("Sending GET request to %s with params %s", self.__audio_endpoint, params)
        response = super()._get(endpoint=f"{self.__audio_endpoint}{params}", headers=token_header)
        return response.json()
