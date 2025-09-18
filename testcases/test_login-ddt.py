import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pageobjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.xlutils import ExcelUtils

class Test_002_DDT_Login:
    base_url = ReadConfig.getApplicationURL()
    path = ".//TESTdata/nop commerece.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_001_login(self, setup):
        self.logger.info("************** Test_002_login **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        self.row= ExcelUtils.get_row_count(self.path, "Sheet1")
        print(self.row)

        list_status=[]

        for r in range(2, self.row+1):
            self.username=ExcelUtils.get_cell_data(self.path, "Sheet1", r, 1)
            self.password=ExcelUtils.get_cell_data(self.path, "Sheet1", r, 2)
            self.exp=ExcelUtils.get_cell_data(self.path, "Sheet1", r, 3)

            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.login()
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp=='pass':
                    self.logger.info("**************** Login Successful **************")

                    self.lp.logout()
                    list_status.append(True)
                elif self.exp=='fail':
                    self.logger.info("**************** Login Failed **************")
                    try:
                        self.lp.logout()
                    except NoSuchElementException:
                        self.logger.warning("Logout button not found, skipping logout.")

                    list_status.append(False)

            elif act_title != exp_title:
               if self.exp=='pass':
                   self.logger.info("**************** Login failed **************")
                   try:
                       self.lp.logout()
                   except NoSuchElementException:
                       self.logger.warning("Logout button not found, skipping logout.")

                   list_status.append(False)
               elif self.exp=='fail':
                   self.logger.info("**************** Login successful **************")
                   try:
                       self.lp.logout()
                   except NoSuchElementException:
                       self.logger.warning("Logout button not found, skipping logout.")

                   list_status.append(True)

        if 'fail' not in list_status:
            self.logger.info("**************** Login DDT IS SUCCESSFUL **************")
            self.driver.quit()
            assert True
        else:
            self.logger.info("**************** Login DDT IS not SUCCESSFUL **************")
            self.driver.quit()
            assert False
        self.logger.info("**************** end of ddt IS SUCCESSFUL **************")

