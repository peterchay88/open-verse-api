import pytest
from src.utils.requests.open_verse_requests import OpenVerseRequests
import logging as logger


@pytest.mark.v1_get_credentails
@pytest.mark.skip
def test_get_v1_token():
    ovr = OpenVerseRequests()
    response = ovr.get_v1_creds(name="peter", description="For Testing", email="peterchay88@gmail.com")
    logger.info(response)

@pytest.mark.v2_get_token
def test_get_v2_token():
    ovr = OpenVerseRequests()
    response = ovr.get_v2_token()
    logger.info(response)