import pytest
from dotenv import load_dotenv
import os
import base64
from src.utils.api_endpoints.register_endpoint import RegisterEndpoint
import datetime
import logging as logger
from src.utils.zephyr.automations_endpoint import AutomationsEndpoint

load_dotenv(f"{os.getcwd()}/secrets.env")
time = datetime.datetime.now()
current_time = f"{time.year}-{time.month}-{time.day}_{time.hour}:{time.minute}:{time.second}"


# --------------------------------------------------------------------------------
# Set and define pytest arguments
# --------------------------------------------------------------------------------

def pytest_addoption(parser):
    parser.addoption("--reports", action="store_true", default=False,
                     help="If flag is set pytest will generate a html report in the reports folder")
    parser.addoption("--xml", action="store_true", default=False,
                     help="If flag is set pytest will generate a Junit XML file in the XML folder")
    parser.addoption("--zephyr", action="store_true", default=False,
                     help="If flag is set pytest will push Junit file to zephyr and create a test cycle base off "
                          "the results"
                          "Need to specify the XML flag as well in order to work as expected.")
    parser.addoption("--page", type=int, default=1, help="Sets what page to return from the response")
    parser.addoption("--page_size", type=int, default=1, help="Sets the number of results to return per page")


@pytest.fixture()
def page(request):
    return request.config.getoption("--page")


@pytest.fixture()
def page_size(request):
    return request.config.getoption("--page_size")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Runs once before any tests are collected or executed.
    Checks to see if the reports and/or xml flag was specified. If so it generates an HTML/XML report.
    :param config:
    :return:
    """
    if config.getoption("--reports"):
        config.option.htmlpath = f"reports/{current_time}_{config.getoption('-m')}_report.html"

    if config.getoption("--xml"):
        config.option.xmlpath = f"xml/{current_time}_{config.getoption('-m')}_report.xml"
        logger.info("Generated XML")


def capitalize_test_names(items):
    """
    Modify test names to be all uppercase. Needed for XML file to be recognized by zephyr.
    :param items:
    :return:
    """
    print("")
    for item in items:
        item.name = item.name.upper()
        item._nodeid = item._nodeid.upper()
        print(item.name)


@pytest.hookimpl
def pytest_collection_modifyitems(items):
    """
    pytest hook function that will be used to modify test attributes
    :param items:
    :return:
    """
    capitalize_test_names(items)


@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    """
    Runs after all tests have been executed.
    if XML and Zephyr flag were specified pushes generated XML to Zephyr
    :param config:
    :return:
    """
    logger.basicConfig(level=logger.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    log = logger.getLogger(__name__)

    if config.getoption("--zephyr"):
        try:
            zephyr = AutomationsEndpoint()
            response = \
                zephyr.upload_junit_xml(project_key="OVA", file=f"{current_time}_{config.getoption('-m')}_report.xml")
            log.info("Push to zephyr successful!")
            log.info(response)
            log.info(response.json())
            # TODO: Figure out why logs do not write to CLI on successful push to zephyr
        except FileNotFoundError as e:
            log.error(f"Error nothing to push up to zephyr, please make sure you ran test with '--xml' flag: {e}")


# --------------------------------------------------------------------------------
# Define fixtures for fetching auth token
# --------------------------------------------------------------------------------

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
        "Content-Type": "application/x-www-form-urlencoded",
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
        "grant_type": "client_credentials"
    }
    ovr = RegisterEndpoint()
    token = ovr.post(endpoint=ovr.token_endpoint,
                     headers=build_token_header,
                     data=data)
    yield token.json()['access_token']


@pytest.fixture(scope="session")
def v2_header(fetch_v2_token, request, **kwargs):
    """
    Creates the header necessary for V2 api requests
    :param request:
    :param fetch_v2_token:
    :return:
    """
    header = {
        "Authorization": f"Bearer {fetch_v2_token}"
    }
    logger.info("Auth header fetched.")
    yield header
    logger.info("Test is done")
