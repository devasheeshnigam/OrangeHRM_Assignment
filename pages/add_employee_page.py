# ===================== pages/add_employee_page.py =====================
from selenium.webdriver.common.by import By

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, first, last):
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.save_button).click()

