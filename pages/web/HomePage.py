from selenium.webdriver.common.by import By

from pages.web.RegistrationPage import RegistrationPage
from pages.web.SearchResultsPage import SearchResultsPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    hotelTab = (By.XPATH, "//a[@data-name='hotels']")
    destination = (By.XPATH, "(//a[@class='select2-choice'])[1]")
    selectDestination = (By.XPATH,"(//div[@class = 'select2-result-label'])[2]")
    checkinCalender = (By.XPATH, "(//label[text()='Check in']/following-sibling::div)[2]//i[@class='bx bx-calendar']")
    checkoutCalender = (By.XPATH, "(//label[text()='Check out']/following-sibling::div)[2]//i[@class='bx bx-calendar']")
    checkin = (By.ID, "checkin")
    checkout = (By.ID, "checkout")
    search = (By.XPATH, "(//button[@class = 'btn btn-primary btn-block' and contains(text(),'Search')])[1]")
    myAccount = (By.XPATH, "//*[@id = 'dropdownCurrency']/i")
    signUp = (By.XPATH, "//a[text()='Sign Up']")

    def getFirstName(self):
        return self.driver.find_element(*HomePage.firstName)

    def getHotelTab(self):
        return self.driver.find_element(*HomePage.hotelTab)

    def getDestination(self):
        return self.driver.find_element(*HomePage.destination)

    def getSelectDestination(self):
        return self.driver.find_element(*HomePage.selectDestination)

    def getChekIn(self):
        return self.driver.find_element(*HomePage.checkin)

    def getCheckOut(self):
        return self.driver.find_element(*HomePage.checkout)

    def getCheckInCalendar(self):
        return self.driver.find_element(*HomePage.checkinCalender)

    def getCheckOutCalender(self):
        return self.driver.find_element(*HomePage.checkoutCalender)

    def getSearchButton(self):
        self.driver.find_element(*HomePage.search).click()
        return SearchResultsPage(self.driver)

    def getMyAccount(self):
        return self.driver.find_element(*HomePage.myAccount)

    def getSignUpButton(self):
        self.driver.find_element(*HomePage.signUp).click()
        return RegistrationPage(self.driver)