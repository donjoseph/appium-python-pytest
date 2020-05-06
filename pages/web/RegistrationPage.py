from selenium.webdriver.common.by import By
from pages.web.AccountPage import AccountPage

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    loginButton = (By.ID, "btn-login")

    firstName = (By.XPATH, "//*[@name='firstname']/following-sibling::span")
    firstNameAfterClick = (By.XPATH, "//*[@name='firstname']")

    lastName = (By.XPATH, "//*[@name='lastname']/following-sibling::span")
    lastNameAfterClick = (By.NAME, "lastname")

    email = (By.XPATH, "//*[@name='email']/following-sibling::span")
    emailAfterClick = (By.NAME,"email")

    phone = (By.XPATH,"//*[@name='phone']/following-sibling::span")
    phoneAfterClick =  (By.NAME,"phone")

    password = (By.XPATH,"//*[@name='password']/following-sibling::span")
    passwordAfterClick = (By.NAME,"password")

    confirmPassword = (By.XPATH, "//*[@name='confirmpassword']/following-sibling::span")
    confirmPasswordAfterClick = (By.NAME, "confirmpassword")

    signUpButton = (By.XPATH, "//button[@class='signupbtn btn_full btn btn-success btn-block btn-lg']")

    def getLoginButton(self):
        return self.driver.find_element(*RegistrationPage.loginButton)

    def getFirstName(self):
        return self.driver.find_element(*RegistrationPage.firstName)

    def getFirstNameAfterClick(self):
        return self.driver.find_element(*RegistrationPage.firstNameAfterClick)

    def getLastName(self):
        return self.driver.find_element(*RegistrationPage.lastName)

    def getLastNameAfterClick(self):
        return self.driver.find_element(*RegistrationPage.lastNameAfterClick)

    def getEmail(self):
        return self.driver.find_element(*RegistrationPage.email)

    def getEmailAfterClick(self):
        return self.driver.find_element(*RegistrationPage.emailAfterClick)

    def getPhone(self):
        return self.driver.find_element(*RegistrationPage.phone)

    def getPhoneAfterClick(self):
        return self.driver.find_element(*RegistrationPage.phoneAfterClick)

    def getPassword(self):
        return self.driver.find_element(*RegistrationPage.password)

    def getPasswordAfterClick(self):
        return self.driver.find_element(*RegistrationPage.passwordAfterClick)

    def getConfirmPassword(self):
        return self.driver.find_element(*RegistrationPage.confirmPassword)

    def getConfirmPasswordAfterClick(self):
        return self.driver.find_element(*RegistrationPage.confirmPasswordAfterClick)

    def getSignUpButton(self):
        self.driver.find_element(*RegistrationPage.signUpButton).click()
        return AccountPage(self.driver)


