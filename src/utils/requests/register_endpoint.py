import logging as logger
from src.utils.requests.base_requests import BaseRequests


class RegisterEndpoint(BaseRequests):

    def __init__(self):
        super().__init__()
        self.__register_endpoint = "v1/auth_tokens/register/"
        self.__token_endpoint = "v1/auth_tokens/token/"

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    def url(self):
        return super().base_url() + self.register_endpoint()

    def register_endpoint(self):
        return self.__register_endpoint

    def token_endpoint(self):
        return self.__token_endpoint


    # ------------------------------------------------------------------------
    # Methods for tests
    # ------------------------------------------------------------------------

    def get_v1_creds(self, name : str, description : str, email : str):
        """
        Sends a POST request to register a user to the open verse api.
        Expected status code for successful request is 201
        :return:
        """
        data = {
            "name": name,
            "description": description,
            "email": email
        }
        response = self.post(endpoint=self.__register_endpoint, data=data, expected_status_code=201)
        return response.json()
