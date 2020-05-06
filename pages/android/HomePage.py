from appium.webdriver.common.mobileby import MobileBy


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    preference = (MobileBy.XPATH, "//*[@text='Preference']")
    preferenceDependecy = (MobileBy.XPATH, "//*[@text='3. Preference dependencies']")
    wifiCheckBox = (MobileBy.ID, "android:id/checkbox")
    wifiSettings = (MobileBy.XPATH, "(//android.widget.RelativeLayout)[2]")
    wifiSettingsName = (MobileBy.ID, "android:id/edit")
    okButton = (MobileBy.XPATH, "//*[@text='OK']")

    def getPreference(self):
        return self.driver.find_element(*HomePage.preference)

    def getPreferenceDependecy(self):
        return self.driver.find_element(*HomePage.preferenceDependecy)

    def getWifiCheckBox(self):
        return self.driver.find_element(*HomePage.wifiCheckBox)

    def getWifiSettings(self):
        return self.driver.find_element(*HomePage.wifiSettings)

    def getWifiSettingsName(self):
        return self.driver.find_element(*HomePage.wifiSettingsName)

    def getOkButton(self):
        return self.driver.find_element(*HomePage.okButton)