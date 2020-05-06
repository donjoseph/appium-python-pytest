import pytest

from pages.android.HomePage import HomePage
from utilities import GenericMethods
from utilities.BaseClassAndroid import BaseClassAndroid


class TestAndroid(BaseClassAndroid):

    # open preference
    # open preference dependencies
    # update wifi settings name
    # go back to preference page
    # @param getWifiData to generate test data for wifi settings name
    def test_WifiSettings(self, getWifiData):
        log = self.log
        driver = self.driver
        homePage = HomePage(driver)
        log.info("home page opened".center(100, "-"))
        homePage.getPreference().click()
        homePage.getPreferenceDependecy().click()
        homePage.getWifiCheckBox().click()
        homePage.getWifiSettings().click()
        homePage.getWifiSettingsName().send_keys(getWifiData["wifiSettings"])
        homePage.getOkButton().click()
        assert homePage.getWifiSettings().is_displayed(), "wifi settings not updated"
        log.info("wifi settings updated".center(100, "-"))
        homePage.getWifiCheckBox().click()
        driver.back()
        driver.back()
        assert homePage.getPreference().is_displayed(), "Homepage is not loaded"
        log.info("Landed back in HomePage".center(100, "-"))

    # generate test data for wifi settings
    @pytest.fixture(params=GenericMethods.getSampleWifiSettings(3))
    def getWifiData(self, request):
        return request.param
