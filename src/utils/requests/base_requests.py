from urllib.request import Request

import requests
import logging as logger
from typing import Protocol


class BaseRequests(Protocol):

    def __init__(self):
        # self.__base_url = "https://api.openverse.org/"
        # self.requests = requests.session()
        pass

    # # ------------------------------------------------------------------------
    # # Getter methods
    # # ------------------------------------------------------------------------
    # def base_url(self):
    #     return self.__base_url

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------
    def get(self, endpoint : str, expected_status_code:int = 200, **kwargs) -> request:
        """
        Wrapper for GET requests
        :return:
        """
        # response = self.requests.get(url=f"{self.__base_url}{endpoint}", **kwargs)
        # self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        # return response
        pass

    def post(self, endpoint : str, data : str = None, json : dict = None,
              expected_status_code:int = 200, **kwargs) -> Request:
        """
        Wrapper for POST requests
        :return:
        """
        # response = self.requests.post(url=f"{self.__base_url}{endpoint}", data=data,
        #                               json=json, **kwargs)
        # self.__validate_status_code(status_code=response.status_code, expected_status_code=expected_status_code)
        # return response
        pass

    @staticmethod
    def __validate_status_code(status_code : int, expected_status_code : int = 200) -> None:
        """
        Check the returned status code of a request call and assert it against what is expected
        :param status_code:
        :param expected_status_code:
        :return:
        """
        # logger.debug("Checking returned status code %s matches expected status code %s",
        #              status_code, expected_status_code)
        # assert status_code == expected_status_code, \
        #     f"Error! Unexpected value returned for status code. Expected {expected_status_code}. Actual {status_code}."
        pass