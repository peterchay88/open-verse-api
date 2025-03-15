import os
import pytest
from src.utils.api_endpoints.register_endpoint import RegisterEndpoint
import logging as logger
from src.utils.helpers.random_generator import RandomGenerator
from dotenv import load_dotenv

load_dotenv("/Users/peter/apps/open-verse-api/secrets.env")
email = os.environ.get("EMAIL")


class TestRegisterUser:

    @pytest.mark.register_user_positive
    def test_register_new_user_ova_t2(self):
        """
        This test generates a random name and creates an open verse api account.
        1. Generate random name
        :return:
        """
        ovr = RegisterEndpoint()
        random_name = RandomGenerator.random_name()
        logger.info("Random name generated: %s", random_name)
        response = ovr.get_v1_creds(name=random_name, description="For Testing", email=email)
        logger.info(response)
        assert response['name'] == random_name, \
            f"Error name returned does not match name given. Expected: {random_name}. Actual {response['name']}."
        assert response['msg'] == "Check your email for a verification link.", \
            f"Error msg key contains unexpected value."

    @pytest.mark.register_user_negative
    def test_register_user_already_exists(self):
        pass


@pytest.mark.v2_get_token
def test_get_v2_token(fetch_v2_token):
    logger.info(fetch_v2_token)

