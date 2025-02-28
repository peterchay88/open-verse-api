import pytest
from dotenv import load_dotenv
import os
import base64
from src.utils.requests.register_endpoint import RegisterEndpoint


load_dotenv("/home/exolab/git-repo/open-verse-api/secrets.env")

@pytest.fixture(scope="session")
def build_token_header():
    """
    Takes the client id and client secret and encodes them and returns them
    in a header used for fetching the v2 token
    :return:
    """
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")
    encoded_creds = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_creds}"
    }

    return headers


@pytest.fixture(scope="session")
def fetch_v2_token(build_token_header):
    """
    Fetches the v2 API token and returns it to other requests.
    :return:
    """
    data = {
        "grant_type" : "client_credentials"
    }
    ovr = RegisterEndpoint()
    token = ovr._post(endpoint=ovr.token_endpoint(),
                      headers=build_token_header,
                      data=data)
    yield token.json()['access_token']


@pytest.fixture(scope="session")
def v2_header(fetch_v2_token, **kwargs):
    """
    Creates the header necessary for V2 api requests
    :param fetch_v2_token:
    :return:
    """
    header = {
        "Authorization": f"Bearer {fetch_v2_token}"
    }

    yield header




