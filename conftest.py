# external imports
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# internal imports
import share


# save arguments from commands line
def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default="chrome",
                     help="Choose: chrome, firefox, safari, chrome106, firefox99, etc ...")

    parser.addoption('--env', action='store', default="prod",
                     help="Choose: test, prod, etc ...")


@pytest.fixture(scope="function")
def driver(request):

    """
    Here browser will
    start and quit
    """

    options = Options()
    command_line_driver = request.config.getoption("driver")  # read driver name from command line

    if command_line_driver == "chrome":
        # open local chrome
        options.add_argument('window-size=1920,1080')
        driver = webdriver.Chrome(
            service=Service('/usr/local/bin/chromedriver'),
            options=options
        )
    elif command_line_driver == "safari":
        # open local safari
        driver = webdriver.Safari(
            service=Service('/usr/bin/safaridriver')
        )
    elif command_line_driver == "firefox":
        # open local firefox
        driver = webdriver.Firefox(
            service=Service('/usr/local/bin/geckodriver')
        )
    else:
        # set capabilities
        options.set_capability('browserName', share.configuration['selenoid_options'][command_line_driver]['browserName'])
        options.set_capability('browserVersion', share.configuration['selenoid_options'][command_line_driver]['browserVersion'])
        options.set_capability('platformName', share.configuration['selenoid_options'][command_line_driver]['platformName'])
        options.set_capability('selenoid:options', share.configuration['selenoid_options'][command_line_driver]['selenoid:options'])
        # open remote selenoid
        driver = webdriver.Remote(
            command_executor=f"http://{share.configuration['aws_test_server_ip']}:4444/wd/hub",
            options=options
        )

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def env(request):
    return share.configuration['env_options'][request.config.getoption("env")]