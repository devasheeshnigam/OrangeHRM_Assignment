
# ===================== pages/login_page.py =====================
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


# ===================== pages/dashboard_page.py =====================
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")

    def navigate_to_pim(self):
        ActionChains(self.driver).move_to_element(self.driver.find_element(*self.pim_tab)).click().perform()


# ===================== pages/pim_page.py =====================
from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")

    def click_add_employee(self):
        self.driver.find_element(*self.add_employee_button).click()


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


# ===================== pages/employee_list_page.py =====================
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


# ===================== tests/test_employee_workflow.py =====================
import time
from utils.driver_setup import DriverSetup
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_list_page import EmployeeListPage

# Test Data
employees = [
    {"first": "John", "last": "Doe"},
    {"first": "Jane", "last": "Smith"},
    {"first": "Alice", "last": "Johnson"},
    {"first": "Bob", "last": "Brown"}
]

def test_employee_workflow():
    driver = DriverSetup.get_driver()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    login.login("Admin", "admin123")

    dashboard = DashboardPage(driver)
    time.sleep(2)
    dashboard.navigate_to_pim()

    pim = PimPage(driver)
    time.sleep(2)
    pim.click_add_employee()

    add_emp = AddEmployeePage(driver)
    for emp in employees:
        time.sleep(2)
        add_emp.add_employee(emp['first'], emp['last'])
        time.sleep(2)
        dashboard.navigate_to_pim()
        time.sleep(2)
        pim.click_add_employee()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    emp_list = EmployeeListPage(driver)
    for emp in employees:
        emp_list.verify_employee(f"{emp['first']} {emp['last']}")

    # Log out
    driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[text()='Logout']").click()
    driver.quit()