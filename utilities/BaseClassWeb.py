import time

import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec



@pytest.mark.usefixtures("setupWebDriver")
class BaseClassWeb:

    def verifyLinkPresence(self, linktext):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.LINK_TEXT, linktext)))

    def selectFromDropDown(self, selectContext, index):
        select = Select(selectContext)
        select.select_by_index(index)

    def wait_for(self,condition_function):
        start_time = time.time()
        while time.time() < start_time + 3:
            if condition_function():
                return True
            else:
                time.sleep(0.1)
        raise Exception(
            'Timeout waiting for {}'.format(condition_function.__name__)
        )

    def page_has_loaded(self):
        page_state = self.driver.execute_script(
            'return document.readyState;'
        )
        return page_state == 'complete'
