import requests
import os
from dotenv import load_dotenv


class OpenVerseRequests:

    def __init__(self):
        self.__url = "https://api.openverse.org/"
        self.__register_endpoint = "v1/auth_tokens/register/"
        self.token_endpoint = "v1/auth_tokens/token/"
        self.request = requests

    def _get(self, endpoint):
        pass

    def _post(self, endpoint, payload, headers=None):
        response = self.request.post(url=f"{self.__url}{endpoint}", headers=headers,
                                     data=payload)
        return response

    def get_v1_creds(self, name : str, description : str, email : str):
        """
        Sends a post request to register a user to the open verse api
        :return:
        """
        data = {
            "name": name,
            "description": description,
            "email": email
        }
        response = self._post(endpoint=self.__register_endpoint, payload=data)
        return response.json()

    def get_v2_token(self):
        """
        Passes the credentials from V1 to fetch the V2 API token.
        :return:
        """
        load_dotenv("../../../secrets.env")
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")

        headers = {
            "Content-Type" : "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": f"client_credentials&client_id={client_id}&client_secret={client_secret}"
        }

        response = self._post(endpoint=self.token_endpoint, payload=data, headers=headers)
        return response.json()









