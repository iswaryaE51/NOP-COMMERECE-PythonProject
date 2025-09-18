import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from pageobjects.LoginPage import LoginPage
from pageobjects.addcustomerpage import AddCustomerPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import random
import string
from selenium.webdriver.support import expected_conditions as EC

class Test_003_AddCustomerPage:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_003_addcustomer(self, setup):
        try:
            self.logger.info("************** Test_003_Add Customer **************")

            self.driver = setup
            self.driver.get(self.base_url)
            self.driver.maximize_window()

            # --- Login ---
            self.lp = LoginPage(self.driver)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.login()
            self.logger.info("************** Successfully logged in **************")

            # --- Navigate to Add Customer ---
            self.addcustomer = AddCustomerPage(self.driver)
            self.addcustomer.open_customer_menu()
            self.addcustomer.open_customer_list()
            self.addcustomer.click_add_new()
            self.logger.info("*************** Navigated to Add Customer Page ***************")

            # --- Fill customer details ---
            self.addcustomer.enter_email(self._generate_random_email())
            self.addcustomer.enter_password(self._generate_random_password())
            self.addcustomer.enter_first_name("Raja")
            self.addcustomer.enter_last_name("Ram")
            self.addcustomer.select_gender("Male")
            self.addcustomer.enter_company("rocobutan")
            self.addcustomer.toggle_tax_exempt()
            self.addcustomer.select_newsletter("nop commerce website")
            self.addcustomer.set_customer_roles(["Guests"])
            self.addcustomer.select_vendor("Vendor 1")
            self.addcustomer.toggle_active()
            self.addcustomer.toggle_change_password()
            self.addcustomer.enter_admin_comment("This is a test comment")
            self.addcustomer.save()
            self.message = self.driver.find_element(By.TAG_NAME, "body").text
            print(self.message)
            if "The new customer has been added successfully." in self.message:
                assert True == True
                self.logger.info("Successfully added the new customer successfully.")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" +" test_addcustomerpage_scr.png")
                self.logger.info("Failed to add the new customer successfully.")
                assert True == False




        finally:
            self.driver.quit()

    # --- Helper methods for generating random data ---
    @staticmethod
    def _generate_random_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_string}@gmail.com"

    @staticmethod
    def _generate_random_password(length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))
