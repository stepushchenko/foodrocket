# external imports
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# internal imports
import share


# get arguments from commands line
def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default="chrome",
                     help="Choose: chrome, firefox, safari, chrome106, firefox99, etc..")


@pytest.fixture(scope="function")
def driver(request):

    """
    Here browser will
    start and quit
    """

    # done: надо получить из аргументов команды в терминале названия браузера (selenoid по умолчанию со свежим хромом)
    # done: надо прописать path до каждого из трех браузеров (chrome, safari, firefox на локальной машине)
    # done: надо сделать отсылку на удаленную машину с selenoide
    # done: надо сделать файл с конфигурациями селенойда для передачи данных в селенойд

    options = Options()
    command_line_driver = request.config.getoption("driver")

    if command_line_driver == "chrome":
        # open local chrome
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
        options.set_capability('browserName', share.selenoid_options[command_line_driver]['browserName'])
        options.set_capability('browserVersion', share.selenoid_options[command_line_driver]['browserVersion'])
        options.set_capability('platformName', share.selenoid_options[command_line_driver]['platformName'])
        options.set_capability('selenoid:options', share.selenoid_options[command_line_driver]['selenoid:options'])
        # open remote selenoid
        driver = webdriver.Remote(
            command_executor=f'http://{share.aws_test_server_ip}:4444/wd/hub',
            options=options
        )

    yield driver

    driver.quit()
