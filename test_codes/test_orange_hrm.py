import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep
from test_locators import locators
from test_data import data
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Test_Orange_hrm:
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver =webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    @pytest.fixture
    def login(self,booting_function):
        self.driver.get(data.Orange_hrm_Data().url)
        # sleep(5)
        self.wait.until(EC.presence_of_element_located((By.NAME,locators.Orange_hrm_Locators().username_inputBox))).send_keys(data.Orange_hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators().username_inputBox)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators.password_InputBox).send_keys(data.Orange_hrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.LoginButton).click()
    
    def test_admin_search_validation(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().admin_tab))).click()
        menu_options_flag=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        search_bar_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
        for i in range(len(locators.Orange_hrm_Locators().caps_tabs)):
            search=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
            search.send_keys(Keys.CONTROL + "a")
            search.send_keys(Keys.DELETE)
            search.send_keys(locators.Orange_hrm_Locators().caps_tabs[i])
            menu_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().tabs_xpath[i])))
            if menu_flag:
                print(locators.Orange_hrm_Locators().tabs_xpath[i],"menu_option found")
            else:
                print(locators.Orange_hrm_Locators().tabs_xpath[i],"menu_option not found")

        # for i in range(len(locators.Orange_hrm_Locators().caps_tabs)):
        #     search = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
        #     search.clear()
        #     search.send_keys(locators.Orange_hrm_Locators().caps_tabs[i])
        #     menu_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().tabs_xpath[i])))
        #     if menu_flag:
        #         print(locators.Orange_hrm_Locators().tabs_xpath[i],"menu_option found")
        #     else:
        #         print(locators.Orange_hrm_Locators().tabs_xpath[i],"menu_option not found")






