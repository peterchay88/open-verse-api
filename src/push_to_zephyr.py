from src.utils.zephyr.automations_endpoint import AutomationsEndpoint

if __name__ == "__main__":
    automation = AutomationsEndpoint()
    response = automation.upload_junit_xml(project_key="OVA", file="junitxml_report.xml")
    print(response)
    print(response.json())
