import pytest
import pytest_html
import pytest_metadata
from selenium import webdriver


@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver : webdriver.Chrome()
        print("launching chrome browser")

        return driver


    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox")

        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########## Pytest HTML Report############

def pytest_configure(config):
    config._metadata = {
        "Project": "Nop Commerce",
        "Module": "Customer",
        "Tester": "Jagdish"

    }


@pytest.mark.optionalHook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
