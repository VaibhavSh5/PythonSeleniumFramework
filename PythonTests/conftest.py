import os
import sys

import pytest
from selenium import webdriver
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="my option: Chrome or Firefox"
    )
    parser.addoption("--test_name", action="store", default="TestSP", help="my option: Checkout or TestSP"
                     )


@pytest.fixture
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    test_name = request.config.getoption("test_name")
    if browser_name == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(executable_path=os.path.dirname(os.path.dirname(__file__))+"/Executables/chromedriver", options=options)
        driver.implicitly_wait(20)
        if test_name == "TestSP":
            driver.get("https://qamajorreg.primerevenue.com")
            # driver.find_element_by_id('idToken1').send_keys('vaibhavtestsp')
            # driver.find_element_by_xpath('//input[@type = \'password\']').send_keys('Prime109')
            # driver.find_element_by_id('loginButton_0').click()
        elif test_name == "Checkout":
            driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver
    elif browser_name == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Firefox(executable_path=os.path.dirname(os.path.dirname(__file__))+"/Executables"
                                                                                              "/geckodriver",
                                   options=options)

        driver.implicitly_wait(20)
        if test_name == "TestSP":
            driver.get("https://qamajorreg.primerevenue.com")
            # action = ActionChains(driver)
            # action.move_to_element(driver.find_element_by_id('idToken1')).send_keys('vaibhavtestsp').perform()
            # driver.find_element_by_xpath('//input[@type = \'password\']').send_keys('Prime109')
            # driver.find_element_by_id('loginButton_0').click()
        elif test_name == "Checkout":
            driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver

    yield
    driver.close()
    print('Driver has been closed!!')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img scr="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.save_screenshot(os.path.dirname(os.path.dirname(__file__))+f"/Failure Screenshots/{name}")
