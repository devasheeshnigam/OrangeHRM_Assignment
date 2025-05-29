#  ===================== pages/employee_list_page.py =====================
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class EmployeeListPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")

    def verify_employee(self, name):
        time.sleep(2)
        self.driver.find_element(*self.search_input).send_keys(name)
        self.driver.find_element(*self.search_input).send_keys(Keys.ENTER)
        time.sleep(2)
        if name.lower() in self.driver.page_source.lower():
            print(f"Name Verified: {name}")
