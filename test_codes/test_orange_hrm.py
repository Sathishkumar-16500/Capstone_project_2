import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from time import sleep
from test_locators import locators
from test_data import data
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Test_Orange_hrm:
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver =webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,10)
        self.action = ActionChains(self.driver)
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
    
    def _admin_search_validation(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().admin_tab))).click()
        #--------verifying menu options are present
        menu_options_flag=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        #--------verifying search bar is present
        search_bar_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
        time.sleep(3)

        small_tabs_flag_list=[]
        caps_tabs_flag_list = []

        #-------verifying the individual menus are present after search in lower_case
        for i in range(len(locators.Orange_hrm_Locators().small_tabs)):
            try:
                search=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.DELETE)
                time.sleep(1)
                search.send_keys(locators.Orange_hrm_Locators().small_tabs[i])
                time.sleep(1)
                self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().tabs_xpath[i])))
                print(locators.Orange_hrm_Locators().small_tabs[i],"menu_option found")
                small_tabs_flag_list.append(True)

            except TimeoutException:
                print(locators.Orange_hrm_Locators().small_tabs[i], "menu_option not found")
                small_tabs_flag_list.append(False)
        small_tab_flag=all(small_tabs_flag_list)
        print('-------------------------------###############################------------------------------')
        # -------verifying the individual menus are present after search in upper_case
        for i in range(len(locators.Orange_hrm_Locators().caps_tabs)):
            try:
                search=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().search_bar)))
                search.send_keys(Keys.CONTROL + "a")
                search.send_keys(Keys.DELETE)
                time.sleep(1)
                search.send_keys(locators.Orange_hrm_Locators().caps_tabs[i])
                time.sleep(1)
                self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().tabs_xpath[i])))
                print(locators.Orange_hrm_Locators().caps_tabs[i],"menu_option found")
                caps_tabs_flag_list.append(True)

            except TimeoutException:
                print(locators.Orange_hrm_Locators().caps_tabs[i], "menu_option not found")
                caps_tabs_flag_list.append(False)
        caps_tab_flag=all(caps_tabs_flag_list)

        # -------combining all the result to validate the testcase
        result=[search_bar_flag,menu_options_flag,small_tab_flag,caps_tab_flag]

        if all(result):
            assert True
        else:
            assert False

    def test_user_management_dropdown_validation(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().admin_tab))).click()
        # --------verifying menu options are present
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().user_management_dropdown))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().users_option))).click()
        user_role=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().user_role_dropdown)))
        time.sleep(2)
        self.action.click(user_role).perform()
        time.sleep(2)
        # dropdown = Select(self.driver.find_element(by=By.XPATH,value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'))
        # dropdown.select_by_index(0)
        # selected_option_text = dropdown.first_selected_option.text
        # print(selected_option_text)
        options = user_role.find_elements(by=By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div')
        # options = self.driver.execute_script("return document.querySelectorAll('#my-dropdown .option')")
        for option in options:
            print(option.get_attribute("innerText"))






