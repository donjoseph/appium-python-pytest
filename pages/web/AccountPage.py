from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    accountHeading = (By.XPATH, "//h3[@class='text-align-left']")
    myAccount = (By.XPATH, "//*[@id = 'dropdownCurrency']/i")
    logout = (By.XPATH,"//a[text()='Logout']")
    loginPageElement = (By.XPATH, "//h3[text()='Login']")

    def getAccountHeading(self):
        return self.driver.find_element(*AccountPage.accountHeading)

    def getMyAccount(self):
        return self.driver.find_element(*AccountPage.myAccount)

    def getLogout(self):
        return self.driver.find_element(*AccountPage.logout)

    def getLoginPageElement(self):
        return self.driver.find_element(*AccountPage.loginPageElement)
