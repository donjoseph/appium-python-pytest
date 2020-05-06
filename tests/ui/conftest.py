import pytest
from selenium import webdriver
from appium import webdriver as mobileWebDriver

from config.AndroidConfig import AndroidConfig
from config.WebConfig import WebConfig
from utilities import Log

global driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setupWebDriver(request):
    log = Log.log()
    browserType = request.config.getoption("browser_name")
    if browserType == "chrome":
        driver = webdriver.Chrome(executable_path = WebConfig.chromeDriver)
    elif browserType == "firefox":
        driver = webdriver.Firefox(executable_path= WebConfig.chromeDriver)
    elif browserType == "ie":
        driver = webdriver.Edge(executable_path = WebConfig.chromeDriver)
    else:
        driver = webdriver.Edge(executable_path = WebConfig.chromeDriver)
    driver.maximize_window()
    driver.implicitly_wait(10)  # seconds
    request.cls.driver = driver
    request.cls.log = log
    yield
    driver.quit()


@pytest.fixture(scope="class")
def setupAndroidDriver(request):
    log = Log.log()
    #service = AppiumService()
    #service.start(args=['--address', '127.0.0.1', '-p', str(4723)])
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = AndroidConfig.deviceName
    desired_caps['avd'] = AndroidConfig.avdName
    desired_caps['avdReadyTimeout'] = AndroidConfig.avdTimeOut
    desired_caps['autoGrantPermissions'] = True
    desired_caps['app'] = AndroidConfig.apkLocation

    #desired_caps['appPackage'] = 'com.phptravelsnative'
    #desired_caps['appWaitActivity'] = "*"

    driver = mobileWebDriver.Remote(AndroidConfig.appiumHost, desired_caps)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.log = log
    yield
    driver.quit()
    #service.stop()

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)
