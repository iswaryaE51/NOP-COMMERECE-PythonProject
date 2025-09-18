import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_Login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.smoke
    def test_001_homepage_title(self,setup):
        self.logger.info("************** Test_001_homepage_title **************")
        self.logger.info("************** Verifying homepage_title **************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        self.driver.implicitly_wait(5)
        if act_title == exp_title:
            self.driver.close()
            assert True
            self.logger.info("************** Successfully logged in **************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_001_homepage_title.png")
            self.driver.close()
            self.logger.error("**************** Failed to login  **************")
            assert False

    @pytest.mark.smoke
    def test_001_login(self,setup):
        self.logger.info("************** Test_001_login **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            self.driver.close()
            self.logger.info("**************** Successfully logged in **************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_001_login.png")
            self.driver.close()
            self.logger.error("**************** Failed to login  **************")
            assert False


