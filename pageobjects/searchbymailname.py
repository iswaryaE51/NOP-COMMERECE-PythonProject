from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchByEmailName():

        txtsearchby_email_xpath= "//input[@id='SearchEmail']"
        txtsearchby_fname_xpath= "//input[@id='SearchFirstName']"
        btsearch_xpath= "//button[@id='search-customers']"
        table_xpath = "//table[@id='customers-grid']"
        tablerows_xpath = "//table[@id='customers-grid']//tbody/tr"
        tablecolumns_xpath = " //table[@id='customers-grid']//tbody/tr/td"

        def __init__(self, driver):
            self.driver = driver

        def search_by_email(self, email):
            self.driver.find_element(By.XPATH, self.txtsearchby_email_xpath).click()
            self.driver.find_element(By.XPATH, self.txtsearchby_email_xpath).clear()
            self.driver.find_element(By.XPATH, self.txtsearchby_email_xpath).send_keys(email)
        def search_by_name(self, name):
            self.driver.find_element(By.XPATH, self.txtsearchby_fname_xpath).click()
            self.driver.find_element(By.XPATH, self.txtsearchby_fname_xpath).clear()
            self.driver.find_element(By.XPATH, self.txtsearchby_fname_xpath).send_keys(name)
        def search_customers(self):
            self.driver.find_element(By.XPATH, self.btsearch_xpath).click()
        def getnoofrows(self):
            return len(self.driver.find_elements(By.XPATH, self.tablerows_xpath))
        def getnoofrowcolumns(self):
            return len(self.driver.find_elements(By.XPATH, self.tablecolumns_xpath))

        def searchbyemailid(self, email):
            flag = False
            rows = self.driver.find_elements(By.XPATH, self.tablerows_xpath)
            for index, row in enumerate(rows, start=1):
                # Scroll the row into view
                self.driver.execute_script("arguments[0].scrollIntoView(true);", row)

                # Get email from 2nd column
                emailid = row.find_element(By.XPATH, "./td[2]").text
                if email == emailid:
                    flag = True
                    break
            return flag

        def searchbyfname(self, fname):
            flag = False
            rows = self.driver.find_elements(By.XPATH, self.tablerows_xpath)
            for index, row in enumerate(rows, start=1):
                # Scroll the row into view
                self.driver.execute_script("arguments[0].scrollIntoView(true);", row)

                # Get email from 2nd column
                gfname = row.find_element(By.XPATH, "./td[3]").text
                if gfname == fname:
                    flag = True
                    break
            return flag










