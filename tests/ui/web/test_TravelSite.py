import pytest

from config.WebConfig import WebConfig
from pages.web.HomePage import HomePage
from utilities import GenericMethods
from utilities.BaseClassWeb import BaseClassWeb


class TestHotelScenarios(BaseClassWeb):

    # open home page
    # hit hotel tab
    # enter destination
    # enter check in checkout dates
    # search and list the available hotels
    # @param getTestData to generate random destination
    def test_HotelSearch(self, getTestData):
        log = self.log
        driver = self.driver
        driver.get(WebConfig.siteAddress)
        log.info("home page opened".center(100, "-"))
        homePage = HomePage(driver)

        homePage.getHotelTab().click()
        homePage.getDestination().click()
        homePage.getDestination().send_keys(getTestData["location"])
        homePage.getSelectDestination().click()
        homePage.getChekIn().clear()
        homePage.getChekIn().send_keys(GenericMethods.getFutureDate(days=1))
        homePage.getCheckInCalendar().click()
        homePage.getCheckOut().clear()
        homePage.getCheckOut().send_keys(GenericMethods.getFutureDate(days=3))
        homePage.getCheckOutCalender().click()
        searchPage = homePage.getSearchButton()

        log.info("User completed Search Criteria".center(100, "-"))
        assert searchPage.getModifyButton().is_displayed(), "Search Results page is not loaded"

        hotels = searchPage.getHotelNames()[:10]
        if hotels is None:
            log.info(("There are no hotels available in location " + getTestData["location"]).center(100, "-"))
        else:
            for hotel in hotels:
                log.info((hotel.text + " is available at " + getTestData["location"]).center(100, "-"))

    # open home page
    # hit my account and go to sign up page
    # enter the details of the user
    # register the user and verify
    # @param getTestData to generate fake user details
    def test_UserRegistration(self, getTestData):
        log = self.log
        driver = self.driver
        driver.get(WebConfig.siteAddress)
        log.info("home page opened".center(100, "-"))
        homePage = HomePage(driver)
        homePage.getMyAccount().click()
        signUpPage = homePage.getSignUpButton()
        signUpPage.getFirstName().click()
        signUpPage.getFirstNameAfterClick().send_keys(getTestData["firstName"])
        signUpPage.getLastName().click()
        signUpPage.getLastNameAfterClick().send_keys(getTestData["lastName"])
        signUpPage.getPhone().click()
        signUpPage.getPhoneAfterClick().send_keys(getTestData["phoneNumber"])
        signUpPage.getEmail().click()
        signUpPage.getEmailAfterClick().send_keys(getTestData["email"])
        signUpPage.getPassword().click()
        signUpPage.getPasswordAfterClick().send_keys(getTestData["password"])
        signUpPage.getConfirmPassword().click()
        signUpPage.getConfirmPasswordAfterClick().send_keys(getTestData["password"])
        profilePage = signUpPage.getSignUpButton()

        userFullName = getTestData["firstName"] + " " + getTestData["lastName"]

        log.info(("Sign Up Completed for " + userFullName).center(100, "-"))

        profileGreeting = profilePage.getAccountHeading().text

        assert profileGreeting == "Hi, " + userFullName, "User profile not loaded for " + userFullName

        profilePage.getMyAccount().click()
        profilePage.getLogout().click()

        assert profilePage.getLoginPageElement().is_displayed(), userFullName + " not logged out correctly"

    # generates test data for web test cases
    @pytest.fixture(params=GenericMethods.createSampleUsersWeb(3))
    def getTestData(self, request):
        return request.param
