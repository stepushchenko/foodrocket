# external imports
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.safari.service import Service as SafariService

# internal imports
import share


# save arguments from commands line
def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default="chrome",
                     help="Choose: chrome, firefox, safari, chrome106, firefox99, etc ...")

    parser.addoption('--env', action='store', default="prod",
                     help="Choose: test, prod, etc ...")


def _run_chrome_driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )


def _run_safari_driver():
    return webdriver.Safari(
        service=SafariService(share.configuration['path_to_safari_driver'])
    )


def _run_firefox_driver():
    return webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )


def _run_selenoid_driver(command_line_driver):
    # set capabilities
    options = Options()
    options.set_capability('browserName', share.configuration['selenoid_options'][command_line_driver]['browserName'])
    options.set_capability('browserVersion',
                           share.configuration['selenoid_options'][command_line_driver]['browserVersion'])
    options.set_capability('platformName', share.configuration['selenoid_options'][command_line_driver]['platformName'])
    options.set_capability('selenoid:options',
                           share.configuration['selenoid_options'][command_line_driver]['selenoid:options'])
    # open remote selenoid
    return webdriver.Remote(
        command_executor=f"http://{share.configuration['aws_test_server_ip']}:4444/wd/hub",
        options=options
    )


@pytest.fixture()
def driver(request):

    command_line_driver = request.config.getoption("driver")  # read driver name from command line

    if command_line_driver == "chrome":
        driver = _run_chrome_driver()
    elif command_line_driver == "safari":
        driver = _run_safari_driver()
    elif command_line_driver == "firefox":
        driver = _run_firefox_driver()
    elif command_line_driver in share.configuration['selenoid_supported_drivers']:
        driver = _run_selenoid_driver(command_line_driver)
    else:
        raise ValueError(command_line_driver)

    yield driver

    driver.quit()


@pytest.fixture()
def env(request):
    return share.configuration['env_options'][request.config.getoption("env")]
