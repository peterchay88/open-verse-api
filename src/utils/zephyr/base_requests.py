import os
import requests
import logging as logger
from dotenv import load_dotenv
from typing import Optional

load_dotenv(f"{os.getcwd()}/secrets.env")
zephyr_token = os.environ.get("ZEPHYR_TOKEN")


class ZephyrBaseRequest:

    def __init__(self):
        self.__base_url = "https://api.zephyrscale.smartbear.com/v2"
        self.__requests = requests.session()
        self.__header = {
            "Authorization": f"Bearer {zephyr_token}"
        }

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    def base_url(self):
        return self.__base_url

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------

    def __build_headers(self, additional_headers: Optional[dict[str, str]] = None):
        """
        Build headers for requests, if additional headers are provided,
        they will be added to the default headers.

        Example of additional headers:
        {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        :param additional_headers:
        :return:
        """
        headers = self.__header.copy()
        if additional_headers:
            if type(additional_headers) is not dict:
                raise TypeError("additional_headers must be a dictionary")
            headers.update(additional_headers)
        return headers

    def _get(self, endpoint: str, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for GET requests.
        :return:
        """
        # If user specifies header as a parameter, remove it from kwargs and append it to the header
        headers = self.__build_headers(additional_headers=kwargs.pop("headers", None))

        response = self.__requests.get(url=f"{self.__base_url}{endpoint}", headers=headers, **kwargs)
        self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        return response

    def _post(self, endpoint: str, data=None, json=None, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for POST requests
        :return:
        """
        # If user specifies header as a parameter, remove it from kwargs and append it to the header
        headers = self.__build_headers(additional_headers=kwargs.pop("headers", None))

        response = self.__requests.post(url=f"{self.__base_url}{endpoint}", data=data,
                                        json=json, headers=headers, **kwargs)
        self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        return response

    @staticmethod
    def __validate_status_code(status_code: int, expected_status_code: int = 200):
        """
        Check the returned status code of a request call and assert it against what is expected
        :param status_code:
        :param expected_status_code:
        :return:
        """
        logger.debug("Checking returned status code %s matches expected status code %s",
                     status_code, expected_status_code)
        assert status_code == expected_status_code, \
            f"Error! Unexpected value returned for status code. Expected {expected_status_code}. Actual {status_code}."
