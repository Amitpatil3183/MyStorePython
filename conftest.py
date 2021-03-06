from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:\SeleniumResources\chromedriver.exe")
        driver.maximize_window()
        print("Launching chrome browser.........")

    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path='C:\SeleniumResources\geckodriver.exe')
        driver.maximize_window()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Ie(executable_path='C:\SeleniumResources\IEDriverServer.exe')
        driver.maximize_window()

    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'MyStore'
    config._metadata['Module Name'] = 'Shopping Feature'
    config._metadata['Tester'] = 'Amit'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)