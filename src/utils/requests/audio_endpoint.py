from src.utils.requests.base_requests import BaseRequests
import logging as logger


class AudioEndpoint(BaseRequests):

    def __init__(self):
        super().__init__()
        self.__audio_endpoint = "v1/audio/"

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    @property
    def url(self):
        return super().base_url + self.audio_endpoint

    @property
    def audio_endpoint(self):
        return self.__audio_endpoint

    @audio_endpoint.setter
    def audio_endpoint(self, value: str):
        if isinstance(value, str):
            self.__audio_endpoint = value
        else:
            raise TypeError("Error, audio endpoint value must be a string")

    # ------------------------------------------------------------------------
    # Methods for tests
    # ------------------------------------------------------------------------
    def get_audio_search(self, token_header: dict, params: str = None):
        """
        Hits the get audio endpoint
        :return:
        """
        data = {
            "q": params
        }
        logger.info("Sending GET request to %s with params %s", self.__audio_endpoint, params)
        response = super().get(endpoint=f"{self.__audio_endpoint}", headers=token_header, params=data)
        return response.json()


if __name__ == "__main__":
    audio = AudioEndpoint()
    print(audio.url)
    print(audio.audio_endpoint)

