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
from pageobjects.searchbymailname import SearchByEmailName



class Test_005_SearchCustomer():
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_005_searchcustomerbymail(self, setup):
        try:
            self.logger.info("************** Test_005_search Customer by mailid**************")

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
            self.logger.info("*************** Successfully opened Customer Menu ***************")

            self.searchcustomer = SearchByEmailName(self.driver)
            self.searchcustomer.search_by_email("TfMslV@gmail.com")
            self.searchcustomer.search_customers()
            time.sleep(4)
            status = self.searchcustomer.searchbyemailid("TfMslV@gmail.com")
            assert True == status
            self.logger.info("*************** Successfully search bye mailid ***************")

        finally:
            self.driver.quit()
    # @pytest.mark.xfail(reason="not implemented")
    # def test_006_searchcustomerbyname(self, setup):
    #     try:
    #         self.logger.info("************** Test_006_search Customer by name**************")
    #
    #         self.driver = setup
    #         self.driver.get(self.base_url)
    #         self.driver.maximize_window()
    #
    #         # --- Login ---
    #         self.lp = LoginPage(self.driver)
    #         self.lp.setusername(self.username)
    #         self.lp.setpassword(self.password)
    #         self.lp.login()
    #         self.logger.info("************** Successfully logged in **************")
    #
    #         # --- Navigate to Add Customer ---
    #         self.addcustomer = AddCustomerPage(self.driver)
    #         self.addcustomer.open_customer_menu()
    #         self.addcustomer.open_customer_list()
    #         self.logger.info("*************** Successfully opened Customer Menu ***************")
    #
    #         self.searchcustomer = SearchByEmailName(self.driver)
    #         self.searchcustomer.search_by_name("Blabla")
    #         self.searchcustomer.search_customers()
    #         time.sleep(4)
    #         status = self.searchcustomer.searchbyfname("Blabla")
    #         assert True == status
    #         self.logger.info("*************** Successfully search by name***************")
    #
    #     finally:
    #         self.driver.quit()