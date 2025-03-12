from src.utils.requests.request_blueprint import RequestBluePrint
import requests
import logging as logger


class BaseRequests(RequestBluePrint):

    def __init__(self):
        self.__base_url = "https://api.openverse.org/"
        self.requests = requests.session()

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, value: str):
        if isinstance(value, str):
            self.__base_url = value
        else:
            raise TypeError("Error, base url value must be a string.")

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------
    def get(self, endpoint: str, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for GET requests
        :return:
        """
        response = self.requests.get(url=f"{self.__base_url}{endpoint}", **kwargs)
        self._validate_status_code(response=response, expected_status_code=expected_status_code)
        return response

    def post(self, endpoint: str, data=None, json: dict = None, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for POST requests
        :return:
        """
        response = self.requests.post(url=f"{self.__base_url}{endpoint}", data=data,
                                      json=json, **kwargs)
        self._validate_status_code(response=response, expected_status_code=expected_status_code)
        return response

    def put(self):
        """
        Wrapper for PUT requests
        :return:
        """
        pass

    @staticmethod
    def _validate_status_code(response, expected_status_code: int = 200) -> None:
        """
        Check the returned status code of a request call and assert it against what is expected
        :param response:
        :param expected_status_code:
        :return:
        """
        logger.debug("Checking returned status code %s matches expected status code %s",
                     response, expected_status_code)
        assert response.status_code == expected_status_code, \
            f"Error! Unexpected value returned for status code. Expected {expected_status_code}. Actual {response}." \
            f"Please see returned response JSON for more information: {response.json()}"



if __name__ == "__main__":
    base_request = BaseRequests()
