from abc import ABC, abstractmethod


class RequestBluePrint(ABC):

    @abstractmethod
    def __init__(self):
        pass

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    @property
    @abstractmethod
    def base_url(self):
        pass

    @base_url.setter
    @abstractmethod
    def base_url(self, value: str):
        pass

    # ------------------------------------------------------------------------
    # Base requests
    # ------------------------------------------------------------------------
    @abstractmethod
    def get(self, endpoint: str, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for GET requests
        :return:
        """
        pass

    @abstractmethod
    def post(self, endpoint: str, data: str = None, json: dict = None, expected_status_code: int = 200, **kwargs):
        """
        Wrapper for POST requests
        :return:
        """
        pass

    @abstractmethod
    def put(self):
        """
        Wrapper for PUT requests
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def _validate_status_code(status_code: int, expected_status_code: int = 200) -> None:
        """
        Check the returned status code of a request call and assert it against what is expected
        :param status_code:
        :param expected_status_code:
        :return:
        """
        pass
