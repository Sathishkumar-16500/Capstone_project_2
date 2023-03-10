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
            print("#-----Test_case_passed-----#")
            assert True
        else:
            print("#-----Test_case_failed-----#")
            assert False

    def _user_management_dropdown_validation(self,booting_function,login):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().admin_tab))).click()
        # --------verifying menu options are present
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().user_management_dropdown))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().users_option))).click()
        user_role_flag=None
        status_flag=None
        try:
            user_role=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().user_role_dropdown)))
            time.sleep(2)
            self.action.click(user_role).perform()
            time.sleep(2)
            drop_down_options = user_role.find_elements(by=By.XPATH, value=locators.Orange_hrm_Locators().user_role_dropdown)
            # self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()='ESS']").click()
            time.sleep(5)
            options=[]
            for option in drop_down_options:
                options.append(option.get_attribute("innerText"))
            options=options[1].split("\n")
            options.pop(0)
            print(options)
            # self.action.click(options[0]).perform()
            # time.sleep(5)
            if options==data.Orange_hrm_Data().user_role_expected_options:
                user_role_flag=True
                print('#------user_role_dropdown options has been validated------#\n')
            else:
                user_role_flag=False
                print('#------user_role_dropdown options are not found------#\n')
        except Exception as e:
            print('Cannot able to click the user_role dropdown\n',e)

        try:
            status=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().status_dropdown)))
            time.sleep(2)
            self.action.click(status).perform()
            time.sleep(2)
            drop_down_options = status.find_elements(by=By.XPATH, value=locators.Orange_hrm_Locators().status_dropdown)
            options=[]
            for option in drop_down_options:
                options.append(option.get_attribute("innerText"))
            options=options[1].split("\n")
            options.pop(0)
            print(options)
            if options==data.Orange_hrm_Data().status_expected_options:
                status_flag=True
                print('#------status_dropdown options has been validated------#\n')
            else:
                status_flag=False
                print('#------status_dropdown options are not found------#\n')
        except:
            print('Cannot able to click the status_dropdown\n')

        #--------combining all the result to validate the testcase--------#
        result = [menu_options_flag, user_role_flag, status_flag]

        if all(result):
            print("#-----Test_case_passed-----#\n")
            assert True
        else:
            print("#-----Test_case_failed-----#\n")
            assert False
    def _new_employee_creation(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_list_flag=None
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().pim_xpath))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().add_button))).click()
            # self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().login_details_toggle))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().middlename_textbox))).send_keys(data.Orange_hrm_Data.test_middle_name)
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().lastname_textbox))).send_keys(data.Orange_hrm_Data.test_last_name)
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().employee_id_textbox))).send_keys(data.Orange_hrm_Data.test_employee_id)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_details_toggle))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_status_radio))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_username_textbox))).send_keys(data.Orange_hrm_Data.test_login_username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_textbox))).send_keys(data.Orange_hrm_Data.test_login_password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_confirm_textbox))).send_keys(data.Orange_hrm_Data.test_login_password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_save_button))).click()
            employee_list_flag=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().add_button)))
        except Exception as e:
            print('Cannot be able to Access employee list page, error occurred:',e)
        print(menu_options_flag,employee_list_flag)
        #--------combining all the result to validate the testcase--------#
        result = [menu_options_flag, employee_list_flag]
        #
        if all(result):
            print("#-----Test_case_passed-----#\n")
            assert True
        else:
            print("#-----Test_case_failed-----#\n")
            assert False

    def _employee_details_page(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_info_result=[]
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_xpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().add_button))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().lastname_textbox))).send_keys(data.Orange_hrm_Data.test_last_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().employee_id_textbox))).send_keys(data.Orange_hrm_Data.test_employee_id1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_details_toggle))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_status_radio))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_username_textbox))).send_keys(data.Orange_hrm_Data.test_login_username1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_confirm_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_save_button))).click()
        time.sleep(3)
        for i in range(len(locators.Orange_hrm_Locators().employee_details)):
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().employee_details_xpath[i])))
                print(locators.Orange_hrm_Locators().employee_details[i], "detail found")
                employee_info_result.append(True)
            except Exception as e:
                print(locators.Orange_hrm_Locators().employee_details[i], "detail not found")
                employee_info_result.append(False)
                print(e)
        # except Exception as e:
        #     print('Cannot be able to validate employee details, error occurred:', e)

        if all(employee_info_result):
            print("#-----Test_case_passed-----#\n")
            assert True
        else:
            print("#-----Test_case_failed-----#\n")
            assert False
    def text_box_clearing_and_entering(self,xpath,data):
        textbox=self.wait.until(EC.presence_of_element_located((By.XPATH,xpath)))
        textbox.send_keys(Keys.CONTROL + "a")
        textbox.send_keys(Keys.DELETE)
        textbox.send_keys(data)

    def _employee_personal_details_tab(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_personal_details_result=[]
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_xpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().add_button))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().lastname_textbox))).send_keys(data.Orange_hrm_Data.test_last_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().employee_id_textbox))).send_keys(data.Orange_hrm_Data.test_employee_id1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_details_toggle))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_status_radio))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_username_textbox))).send_keys(data.Orange_hrm_Data.test_login_username1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_confirm_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_save_button))).click()
        time.sleep(3)

        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_first_name_xpath,data=data.Orange_hrm_Data.test_personal_details['first_name'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_middle_name_xpath,data=data.Orange_hrm_Data.test_personal_details['middle_name'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_last_name_xpath,data=data.Orange_hrm_Data.test_personal_details['last_name'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_nick_name_xpath,data=data.Orange_hrm_Data.test_personal_details['nick_name'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_employee_id_xpath,data=data.Orange_hrm_Data.test_personal_details['employee_id'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_other_id_xpath,data=data.Orange_hrm_Data.test_personal_details['other_id'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_driving_license_no_xpath,data=data.Orange_hrm_Data.test_personal_details['license_no'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_license_expiry_date_xpath,data=data.Orange_hrm_Data.test_personal_details['license_expiry_date'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_ssn_no_xpath,data=data.Orange_hrm_Data.test_personal_details['ssn_no'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.personal_details_sin_no_xpath,data=data.Orange_hrm_Data.test_personal_details['sin_no'])

        nationality=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_nationality)
        self.action.click(nationality).perform()
        self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()='Indian']").click()
        time.sleep(2)
        martial_status=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_marital_status)
        self.action.click(martial_status).perform()
        self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()='Single']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_dob).send_keys(data.Orange_hrm_Data.test_personal_details['dob'])
        self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_gender_male).click()
        self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_military_service).send_keys(data.Orange_hrm_Data.test_personal_details['military_service'])
        self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.personal_details_save_button).click()

        for i in range(len(locators.Orange_hrm_Locators.personal_details_xpath_list)):
            info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.personal_details_xpath_list[i]))).get_attribute("value")
            employee_personal_details_result.append(info)
        print('data given to the form:',data.Orange_hrm_Data.personal_details_list)
        print("data present in the form:",employee_personal_details_result)
        print('#--------------###############----------------#')
        if employee_personal_details_result==data.Orange_hrm_Data.personal_details_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False
    def test_employee_contact_details_tab(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_contact_details_result=[]
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().pim_xpath))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().add_button))).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().firstname_textbox))).send_keys(data.Orange_hrm_Data.test_first_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().lastname_textbox))).send_keys(data.Orange_hrm_Data.test_last_name1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().employee_id_textbox))).send_keys(data.Orange_hrm_Data.test_employee_id1)
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_details_toggle))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_status_radio))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_username_textbox))).send_keys(data.Orange_hrm_Data.test_login_username1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_password_confirm_textbox))).send_keys(data.Orange_hrm_Data.test_login_password1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().login_save_button))).click()
        time.sleep(3)

        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.contact_details))).click()
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_street1_xpath, data=data.Orange_hrm_Data.contact_details['street1'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_street2_xpath, data=data.Orange_hrm_Data.contact_details['street2'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_city_xpath, data=data.Orange_hrm_Data.contact_details['city'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_state_xpath, data=data.Orange_hrm_Data.contact_details['state'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_zip_code_xpath, data=data.Orange_hrm_Data.contact_details['zip_code'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_home_no_xpath, data=data.Orange_hrm_Data.contact_details['home_no'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_mobile_no_xpath, data=data.Orange_hrm_Data.contact_details['mobile_no'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_work_no_xpath, data=data.Orange_hrm_Data.contact_details['work_no'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_work_email_xpath, data=data.Orange_hrm_Data.contact_details['work_email'])
        self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.contacts_details_other_email_xpath, data=data.Orange_hrm_Data.contact_details['other_email'])

        country=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.contacts_details_country_xpath)
        self.action.click(country).perform()
        self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()='India']").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.contacts_details_save_btn_xpath).click()

        for i in range(len(locators.Orange_hrm_Locators.contacts_details_xpath_list)):
            info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.contacts_details_xpath_list[i]))).get_attribute("value")
            employee_contact_details_result.append(info)
        print('data given to the form:',data.Orange_hrm_Data.contact_details_list)
        print("data present in the form:",employee_contact_details_result)
        print('#--------------###############----------------#')
        if employee_contact_details_result==data.Orange_hrm_Data.contact_details_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False















