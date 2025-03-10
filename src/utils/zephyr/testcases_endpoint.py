from src.utils.zephyr.base_requests import ZephyrBaseRequest
import logging as logger


class TestCasesEndpoint(ZephyrBaseRequest):

    def __init__(self):
        super().__init__()
        self.__endpoint = "/testcases"

    def endpoint(self):
        return self.__endpoint

    def set_endpoint(self, endpoint: str):
        self.__endpoint = endpoint

    def get_testcase(self, project_key: str, folder_id: int = None, max_results: int = 10, start_at: int = 0):
        data = {
            "projectKey" : project_key,
            "folderID" : folder_id,
            "maxResults" : max_results,
            "startAt" : start_at
        }
        logger.debug("Fetching test cases with the following params: %s", data)
        response = super()._get(endpoint=self.__endpoint, params=data)
        return response


if __name__ == "__main__":
    test = TestCasesEndpoint()
    print(test.get_testcase(project_key="OVA"))
    print(test.get_testcase(project_key="OVA").json())