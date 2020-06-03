import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox", "opera", "yandex"])
    # parser.addoption("--executor", action="store", default="192.168.8.112")
    parser.addoption("--executor", action="store", default="localhost")


@pytest.fixture
def firefox(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def chrome(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def remote(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    # wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
    #                       desired_capabilities={"browserName": browser})  # "platform": "linux"

    # for lambdatest
    # https://www.lambdatest.com/support/docs/pytest-with-selenium-running-pytest-automation-script-on-lambdatest-selenium-grid/

    wd = webdriver.Remote(
        command_executor="https://iamkos:KkxKVVGfuvcGR2XDw7xw8DlLxpgMHX6oGs9dz21x81Hahf5kB9@hub.lambdatest.com/wd/hub",
        desired_capabilities={"platform": "Windows 10", "browserName": "chrome", "version": "73"})

    wd.maximize_window()
    request.addfinalizer(wd.quit)
    return wd
