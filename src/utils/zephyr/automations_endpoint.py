from src.utils.zephyr.base_requests import ZephyrBaseRequest
import logging as logger
import os


class AutomationsEndpoint(ZephyrBaseRequest):

    def __init__(self):
        super().__init__()
        self.__endpoint = "/automations/executions/junit"
        self.__xml_file_path = f"{os.getcwd()}/xml/"

    def endpoint(self):
        return self.__endpoint

    def set_endpoint(self, endpoint: str):
        self.__endpoint = endpoint

    def upload_junit_xml(self, project_key: str, file: str, auto_create_test: bool = False):
        params = {
            "projectKey": project_key,
            "autoCreateTestCases": auto_create_test
        }

        with open(f"{self.__xml_file_path}{file}", "rb") as f:
            files = {"file": f}
            response = super()._post(endpoint=self.__endpoint, files=files, params=params)
            logger.info("Successfully Pushed XML file to Zephyr")

        return response


def main():
    automation = AutomationsEndpoint()
    response = automation.upload_junit_xml(project_key="OVA", file="2025-3-14_22:20:17__report.xml")
    print(response)
    print(response.json())


if __name__ == "__main__":
    main()
