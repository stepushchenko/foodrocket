import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# get arguments from commands line
def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default="chrome",
                     help="Choose: chrome, firefox, safari, chrome106, firefox99, etc..")


@pytest.fixture(scope="function")
def driver(request):

    # todo: надо получить из аргументов команды в терминале названия браузера (selenoid по умолчанию со свежим хромом)
    # todo: надо прописать path до каждого из трех браузеров (chrome, safari, firefox на локальной машине)
    # todo: надо сделать отсылку на удаленную машину с selenoide
    # todo: надо сделать файл с конфигурациями селенойда для передачи данных в селенойд

    driver = None
    command_line_driver = request.config.getoption("driver")

    if command_line_driver == "chrome":
        # open local chrome
        options = Options()
        driver = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver',
            options=options,
        )
    elif command_line_driver == "safari":
        # open local safari
        pass
    elif command_line_driver == "firefox":
        # open local firefox
        pass
    else:
        # open selenoid
        pass

    yield driver

    driver.quit()
