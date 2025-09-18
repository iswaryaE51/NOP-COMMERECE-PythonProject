import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AddCustomerPage:
    # Locators
    link_customer_menu = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_list = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_add_new = "//a[@class='btn btn-primary']"
    txt_email = "//input[@id='Email']"
    txt_password = "//input[@id='Password']"
    txt_first_name = "//input[@id='FirstName']"
    txt_last_name = "//input[@id='LastName']"
    rd_male = "//input[@id='Gender_Male']"
    rd_female = "//input[@id='Gender_Female']"
    txt_company = "//input[@id='Company']"
    cb_tax_exempt = "//input[@id='IsTaxExempt']"
    txt_newsletter = "//input[contains(@class, 'select2-search__field')]"
    customer_roles_select_id = "SelectedCustomerRoleIds"
    dp_vendor = "//select[@id='VendorId']"
    cb_active = "//input[@id='Active']"
    cb_change_password = "//input[@id='MustChangePassword']"
    txt_admin_comment = "//textarea[@id='AdminComment']"
    btn_save = "//button[@name='save']//i[@class='far fa-floppy-disk']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(driver)

    # --- Menu Methods ---
    def open_customer_menu(self):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.link_customer_menu)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.5)

    def open_customer_list(self):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.link_customer_list)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.5)

    def click_add_new(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.link_add_new)))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()
        time.sleep(0.2)

    # --- Input Methods ---
    def enter_email(self, email):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_email)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_password)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(password)

    def enter_first_name(self, firstname):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_first_name)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(firstname)

    def enter_last_name(self, lastname):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_last_name)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(lastname)

    def select_gender(self, gender):
        if gender.lower() == 'male':
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.rd_male)))
        else:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.rd_female)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.2)

    def enter_company(self, company):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_company)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(company)

    def toggle_tax_exempt(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cb_tax_exempt)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.2)

    def select_newsletter(self, newsletter):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_newsletter)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.clear()
            element.send_keys(newsletter)
            element.send_keys(Keys.TAB)
        except TimeoutException:
            self.driver.save_screenshot("error_newsletter.png")
            raise Exception("Newsletter input not found or not interactable.")

    def set_customer_roles(self, roles):
        try:
            select_element = self.wait.until(EC.presence_of_element_located((By.ID, self.customer_roles_select_id)))
            self.driver.execute_script("arguments[0].style.display='block'; arguments[0].scrollIntoView(true);", select_element)
            select = Select(select_element)
            select.deselect_all()
            for role in roles:
                select.select_by_visible_text(role)
        except TimeoutException:
            self.driver.save_screenshot("error_customer_roles.png")
            raise Exception("Customer roles dropdown not found or interactable.")

    def select_vendor(self, vendor_name):
        select_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.dp_vendor)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", select_element)
        drp = Select(select_element)
        drp.select_by_visible_text(vendor_name)

    def toggle_active(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cb_active)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.2)

    def toggle_change_password(self):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.cb_change_password)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        time.sleep(0.2)

    def enter_admin_comment(self, comment):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.txt_admin_comment)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(comment)

    def save(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_save)))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        element.click()
        time.sleep(0.2)

    def success_message(self):
        time.sleep(3)
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self. message)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.text