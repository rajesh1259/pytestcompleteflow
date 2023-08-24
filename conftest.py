import time

import pytest
from _pytest.outcomes import xfail
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions
chrome_options = ChromeOptions()
driver = None





# Specify the path to the WebDriver service executable
#from lamdapro.lamtest import chrome_options
from selenium.webdriver.chrome.options import Options

webdriver_service = Service('/Users/vaibhavlutade/PycharmProjects/pytestproject/currentproj/chromedriver114')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

@pytest.fixture(scope="class")
def mintex(request):
    global driver
    webdriver_service = Service('/Users/vaibhavlutade/PycharmProjects/pytestproject/currentproj/chromedriver114')
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    driver.get("https://staging-cu.reposenergy.com/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver

    # Teardown
    driver.close()


def _capture_screenshot(file_name):
    pass






import pytest

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')  # Fixed the comparison operator from '==' to '='
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:240px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
