from src.utils.api_endpoints.base_requests import BaseRequests


class RegisterEndpoint(BaseRequests):

    def __init__(self):
        super().__init__()
        self.__register_endpoint = "v1/auth_tokens/register/"
        self.__token_endpoint = "v1/auth_tokens/token/"

    # ------------------------------------------------------------------------
    # Getter methods
    # ------------------------------------------------------------------------
    @property
    def url(self):
        return super().base_url() + self.register_endpoint

    @property
    def register_endpoint(self):
        return self.__register_endpoint

    @register_endpoint.setter
    def register_endpoint(self, value: str):
        self.__register_endpoint = value

    @property
    def token_endpoint(self):
        return self.__token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, value: str):
        self.__token_endpoint = value

    # ------------------------------------------------------------------------
    # Methods for tests
    # ------------------------------------------------------------------------

    def get_v1_creds(self, name: str, description: str, email: str):
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
