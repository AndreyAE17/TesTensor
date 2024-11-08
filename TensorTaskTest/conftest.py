import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loguru import logger

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-cache")
    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()
    driver.implicitly_wait(100)
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def log_errors():
    logger.remove()  
    logger.add("logs/logs.log",format="{time} {level} {message}", level="ERROR")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        logger.error(f"Test failed: {item.nodeid}")
        logger.exception(rep.longrepr)