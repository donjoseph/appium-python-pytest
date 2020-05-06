from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    modify = (By.XPATH, "//button[text()='Modify']")
    firstHotelName = (By.XPATH, "//h5/a")

    def getModifyButton(self):
        return self.driver.find_element(*SearchResultsPage.modify)

    def getHotelNames(self):
        return self.driver.find_elements(*SearchResultsPage.firstHotelName)