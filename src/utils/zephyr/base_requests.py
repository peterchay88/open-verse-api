import os

import requests
import logging as logger
from dotenv import load_dotenv

load_dotenv("/home/exolab/git-repo/open-verse-api/secrets.env")
zephyr_token = os.environ.get("ZEPHYR_TOKEN")


class ZephyrBaseRequest:

    def __init__(self):
        self.__base_url = "https://api.zephyrscale.smartbear.com/v2"
        self.__requests = requests.session()
        self.__header = {
            "Authorization" : f"Bearer {zephyr_token}"
        }

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    def base_url(self):
        return self.__base_url

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------
    def _get(self, endpoint : str, expected_status_code:int = 200, **kwargs):
        """
        Wrapper for GET requests
        :return:
        """
        if "content-length" in kwargs:
            self.__header["content-length"] = kwargs["content-length"]

        response = self.__requests.get(url=f"{self.__base_url}{endpoint}", headers=self.__header, **kwargs)
        self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        return response

    def _post(self, endpoint : str, data=None, json=None, expected_status_code:int = 200, **kwargs):
        """
        Wrapper for POST requests
        :return:
        """
        if "content_length" in kwargs:
            self.__header["content_length"] = kwargs["content_length"]
            del(kwargs["content_length"])

        response = self.__requests.post(url=f"{self.__base_url}{endpoint}", data=data,
                                        json=json, headers=self.__header,**kwargs)
        # self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        return response

    @staticmethod
    def __validate_status_code(status_code : int, expected_status_code : int = 200):
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