from importlib.metadata import metadata

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome( options=chrome_options)
        print("Launching Chrome with custom options")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("launching firefox")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("launching edge")
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "NopCommerce Automation Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'NopCommerce Automation'
    metadata['Module Name'] = 'Login Tests'
    metadata['Tester'] = 'Iswarya'
    metadata['Environment'] = 'QA'

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
