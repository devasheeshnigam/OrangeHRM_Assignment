# ===================== tests/test_employee_workflow.py =====================
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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