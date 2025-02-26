import requests
import base64
import logging as logger
import os
from dotenv import load_dotenv


class OpenVerseRequests:

    def __init__(self):
        self.__url = "https://api.openverse.org/"
        self.__register_endpoint = "v1/auth_tokens/register/"
        self.__token_endpoint = "v1/auth_tokens/token/"
        self.__audio_endpoint = "v1/audio/?q="
        self.__request = requests.session()

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    def url(self):
        return self.__url

    def register_endpoint(self):
        return self.__register_endpoint

    def token_endpoint(self):
        return self.__token_endpoint

    def audio_endpoint(self):
        return self.__audio_endpoint

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------
    def _get(self, endpoint, log=True, **kwargs):
        if log:
            logger.debug("Sending GET request with the following params. URL: %s, endpoint: %s",
                         self.__url, endpoint)
        response = self.__request.get(url=f"{self.__url}{endpoint}", **kwargs)
        self.__assert_status_code(status_code=response.status_code)
        return response

    def _post(self, endpoint, data=None, headers=None, json=None, log=True, **kwargs):
        if log:
            logger.debug("Sending POST request with the following params. URL: %s, Endpoint: %s, Headers %s, "
                         "Data %s, JSON: %s", self.__url, endpoint, headers, data, json)
        response = self.__request.post(url=f"{self.__url}{endpoint}", headers=headers,
                                     data=data, json=json, **kwargs)
        self.__assert_status_code(status_code=response.status_code)
        return response

    @staticmethod
    def __assert_status_code(status_code: int, expected_status_code = 200):
        """
        Checks the returned status code passed through and asserts against what is expected.
        :param status_code:
        :param expected_status_code:
        :return:
        """
        assert status_code == expected_status_code, \
            f"Error! Unexpected status code returned. Expected: {expected_status_code}. Acutal: {status_code}."

    # ------------------------------------------------------------------------
    # Methods for tests
    # ------------------------------------------------------------------------

    def get_v1_creds(self, name : str, description : str, email : str):
        """
        Sends a POST request to register a user to the open verse api
        :return:
        """
        data = {
            "name": name,
            "description": description,
            "email": email
        }
        response = self._post(endpoint=self.__register_endpoint, data=data)
        return response.json()


    def get_audio_search(self, token_header, params : str = None, **kwargs):
        """
        Sends a GET request to the audio endpoint.
        :param params:
        :param token_header:
        :param kwargs:
        :return:
        """
        if params is None:
            params = ""

        response = self._get(endpoint=f"{self.__audio_endpoint}{params}", headers=token_header, **kwargs)
        return response.json()









