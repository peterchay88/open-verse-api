import requests
import base64
import logging as logger
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

    def _post(self, endpoint, payload, headers=None, **kwargs):
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
        load_dotenv("/Users/peter/apps/open-verse-api/secrets.env") # Need to use absolute path
        client_id = os.environ.get("CLIENT_ID")
        client_secret = os.environ.get("CLIENT_SECRET")
        logger.info(client_id)
        # Encode credentials
        encoded_creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_creds}"
        }

        data = {
            "grant_type": "client_credentials"
            # "client_id": client_id,
            # "client_secret": client_secret
        }

        response = self._post(endpoint=self.token_endpoint, payload=data, headers=headers)
        return response.json()









