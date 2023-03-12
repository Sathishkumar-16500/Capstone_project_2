import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException

from test_locators import locators
from test_data import data
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


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


    
    def test_admin_search_validation(self,booting_function,login):
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

    def test_user_management_dropdown_validation(self,booting_function,login):
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
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()='ESS']").click()
            time.sleep(3)
            options=[]
            for option in drop_down_options:
                options.append(option.get_attribute("innerText"))
            options=options[1].split("\n")
            options.pop(0)
            print(options)
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

    def test_new_employee_creation(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_list_flag=None
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().pim_xpath))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().add_button))).click()
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
            employee_list_flag=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators().personal_details_heading)))
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

    def test_employee_details_page(self,booting_function,login):
        menu_options_flag = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators().menu_options)))
        employee_info_result=[]
        try:
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
                    print(locators.Orange_hrm_Locators().employee_details[i],e, "detail not found")
                    employee_info_result.append(False)
                    print(e)
        except Exception as e:
            print('Cannot be able to validate employee details, error occurred:', e)
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

    def test_employee_personal_details_tab(self,booting_function,login):
        employee_personal_details_result=[]
        try:
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
                try:
                    info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.personal_details_xpath_list[i]))).get_attribute("value")
                    employee_personal_details_result.append(info)
                except Exception as e:
                    print(e)
            print('data given to the form:',data.Orange_hrm_Data.personal_details_list)
            print("data present in the form:",employee_personal_details_result)
            print('#--------------###############----------------#')
        except Exception as e:
            print('Cannot be able to validate employee perosnal details, error occurred:', e)
        if employee_personal_details_result==data.Orange_hrm_Data.personal_details_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False

    def test_employee_contact_details_tab(self,booting_function,login):
        employee_contact_details_result=[]
        try:
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
                try:
                    info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.contacts_details_xpath_list[i]))).get_attribute("value")
                    employee_contact_details_result.append(info)
                except Exception as e:
                    print(e)
            print('data given to the form:',data.Orange_hrm_Data.contact_details_list)
            print("data present in the form:",employee_contact_details_result)
            print('#--------------###############----------------#')
        except Exception as e:
            print('Cannot be able to validate employee contact details, error occurred:', e)
        if employee_contact_details_result==data.Orange_hrm_Data.contact_details_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False

    def test_employee_emergency_contacts_tab(self,booting_function,login):
        employee_emergency_contact_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.emergency_contacts))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.emergency_contacts_add_btn_xpath))).click()
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.emergency_contacts_name_xpath, data=data.Orange_hrm_Data.emergency_contact['name'])
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.emergency_contacts_relationship_xpath, data=data.Orange_hrm_Data.emergency_contact['relationship'])
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.emergency_contacts_home_telephone_xpath, data=data.Orange_hrm_Data.emergency_contact['home_telephone'])
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.emergency_contacts_mobile_xpath, data=data.Orange_hrm_Data.emergency_contact['mobile'])
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.emergency_contacts_work_telephone_xpath, data=data.Orange_hrm_Data.emergency_contact['work_telephone'])

            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.emergency_contacts_save_btn_xpath).click()

            for i in range(len(locators.Orange_hrm_Locators.emergency_contacts_result_list)):
                try:
                    info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.emergency_contacts_result_list[i]))).text
                    employee_emergency_contact_result.append(info)
                except Exception as e:
                    print(e)
            print('data given to the form:',data.Orange_hrm_Data.emergency_contact_list)
            print("data present in the form:",employee_emergency_contact_result)
            print('#--------------###############----------------#')
        except Exception as e:
            print('Cannot be able to validate employee emergency contact details, error occurred:', e)
        if employee_emergency_contact_result==data.Orange_hrm_Data.emergency_contact_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False

    def test_employee_dependants_tab(self,booting_function,login):
        employee_dependants_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.dependants))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.dependants_add_btn_xpath))).click()
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.dependants_name_xpath, data=data.Orange_hrm_Data.dependants['name'])
            self.text_box_clearing_and_entering(xpath=locators.Orange_hrm_Locators.dependants_dob_xpath, data=data.Orange_hrm_Data.dependants['dob'])
            relationship = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.dependants_relationship_xpath)
            self.action.click(relationship).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()='Child']").click()
            time.sleep(3)

            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.dependants_save_btn_xpath).click()

            for i in range(len(locators.Orange_hrm_Locators.dependants_result_list)):
                try:
                    info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.dependants_result_list[i]))).text
                    employee_dependants_result.append(info)
                except Exception as e:
                    print(e)
            print('data given to the form:',data.Orange_hrm_Data.dependants_list)
            print("data present in the form:",employee_dependants_result)
            print('#--------------###############----------------#')
        except Exception as e:
            print('Cannot be able to validate employee dependants details, error occurred:', e)
        if employee_dependants_result==data.Orange_hrm_Data.dependants_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False

    def test_employee_job_details_tab(self,booting_function,login):
        employee_job_details_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job))).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_joined_date))).send_keys(data.Orange_hrm_Data.job_details['joined_date'])
            time.sleep(2)
            job_title=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_title_dropdown)
            self.action.click(job_title).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()="+"'"+data.Orange_hrm_Data.job_details['job_title']+"']").click()
            time.sleep(2)
            job_category = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_category_dropdown)
            self.action.click(job_category).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['job_category']+"']").click()
            time.sleep(2)
            sub_unit = self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.job_details_sub_unit_dropdown)
            self.action.click(sub_unit).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['sub_unit']+"']").click()
            time.sleep(2)
            location = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_location_dropdown)
            self.action.click(location).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['location']+"']").click()
            time.sleep(2)
            employee_status = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_employment_status_dropdown)
            self.action.click(employee_status).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['employment_status']+"']").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_include_toggle).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_contract_start_date))).send_keys(data.Orange_hrm_Data.job_details['contract_start_date'])
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_contract_end_date).send_keys(data.Orange_hrm_Data.job_details['contract_end_date'])

            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_save_btn).click()

            for i in range(len(locators.Orange_hrm_Locators.job_details_list)):
                try:
                    if locators.Orange_hrm_Locators.job_details_list[i].endswith('div'):
                        info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_list[i]))).text
                        employee_job_details_result.append(info)
                    elif locators.Orange_hrm_Locators.job_details_list[i].endswith('input'):
                        info = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.job_details_list[i]))).get_attribute("value")
                        employee_job_details_result.append(info)
                except Exception as e:
                    print(e)

            print('data given to the form:', data.Orange_hrm_Data.job_details_list)
            print("data present in the form:", employee_job_details_result)
            print('#--------------###############----------------#')
        except Exception as e:
            print('Cannot be able to validate employee job details, error occurred:', e)
        if employee_job_details_result==data.Orange_hrm_Data.job_details_list:
            print("the data entered have been displayed and validated")
            assert True
        else:
            print("the data entered is not displayed correctly")
            assert False

    def test_employee_job_details_termination(self,booting_function,login):
        employee_job_termination_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job))).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_joined_date))).send_keys(data.Orange_hrm_Data.job_details['joined_date'])
            time.sleep(2)
            job_title=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_title_dropdown)
            self.action.click(job_title).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()="+"'"+data.Orange_hrm_Data.job_details['job_title']+"']").click()
            time.sleep(2)
            job_category = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_category_dropdown)
            self.action.click(job_category).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['job_category']+"']").click()
            time.sleep(2)
            sub_unit = self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.job_details_sub_unit_dropdown)
            self.action.click(sub_unit).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['sub_unit']+"']").click()
            time.sleep(2)
            location = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_location_dropdown)
            self.action.click(location).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['location']+"']").click()
            time.sleep(2)
            employee_status = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_employment_status_dropdown)
            self.action.click(employee_status).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['employment_status']+"']").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_include_toggle).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_contract_start_date))).send_keys(data.Orange_hrm_Data.job_details['contract_start_date'])
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_contract_end_date).send_keys(data.Orange_hrm_Data.job_details['contract_end_date'])

            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_save_btn).click()

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_terminate_employee))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_termination_date))).send_keys(data.Orange_hrm_Data.job_termination['termination_date'])
            termination_reason=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.job_details_termination_reason_dropdown)))
            self.action.click(termination_reason).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_termination['termination_reason']+"']").click()
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_termination_save_btn).click()

            termination_date=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_termination_date_result))).text
            activate_employment=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_activate_employee_btn)

            if termination_date.endswith(data.Orange_hrm_Data.job_termination['termination_date']):
                employee_job_termination_result.append(True)
            else:
                employee_job_termination_result.append(False)

            if activate_employment:
                employee_job_termination_result.append(True)
            else:
                employee_job_termination_result.append(False)

            print(employee_job_termination_result,'dsd')

        except Exception as e:
            print('Cannot be able to validate employee job termination, error occurred:', e)
        if all(employee_job_termination_result):
            print("#-----Test_case_passed-----#\n")
            assert True
        else:
            print("#-----Test_case_failed-----#\n")
            assert False

    def test_employee_job_details_activation(self,booting_function,login):
        terminate_employment=None
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job))).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_joined_date))).send_keys(data.Orange_hrm_Data.job_details['joined_date'])
            time.sleep(2)
            job_title=self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_title_dropdown)
            self.action.click(job_title).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()="+"'"+data.Orange_hrm_Data.job_details['job_title']+"']").click()
            time.sleep(2)
            job_category = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_job_category_dropdown)
            self.action.click(job_category).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['job_category']+"']").click()
            time.sleep(2)
            sub_unit = self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.job_details_sub_unit_dropdown)
            self.action.click(sub_unit).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['sub_unit']+"']").click()
            time.sleep(2)
            location = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_location_dropdown)
            self.action.click(location).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['location']+"']").click()
            time.sleep(2)
            employee_status = self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_employment_status_dropdown)
            self.action.click(employee_status).perform()
            self.driver.find_element(by=By.XPATH,value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_details['employment_status']+"']").click()
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_include_toggle).click()
            time.sleep(2)
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_contract_start_date))).send_keys(data.Orange_hrm_Data.job_details['contract_start_date'])
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_contract_end_date).send_keys(data.Orange_hrm_Data.job_details['contract_end_date'])

            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_save_btn).click()

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_terminate_employee))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_termination_date))).send_keys(data.Orange_hrm_Data.job_termination['termination_date'])
            termination_reason=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.job_details_termination_reason_dropdown)))
            self.action.click(termination_reason).perform()
            self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()="+"'"+ data.Orange_hrm_Data.job_termination['termination_reason']+"']").click()
            self.driver.find_element(by=By.XPATH,value=locators.Orange_hrm_Locators.job_details_termination_save_btn).click()
            time.sleep(3)
            activate_employment=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.job_details_activate_employee_btn)))
            activate_employment.click()

            terminate_employment=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.job_details_terminate_employee)))
        except Exception as e:
            print('Cannot be able to validate employee job activation, error occurred:', e)

        if terminate_employment:
            print("Employee activated successfully")
            assert True
        else:
            print("Employee not activated")
            assert False
    def test_employee_salary_details(self,booting_function,login):
        salary_details_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_details_add_btn))).click()
            for i in range(len(locators.Orange_hrm_Locators.salary_details_list)):
                if locators.Orange_hrm_Locators.salary_details_list[i].endswith('input'):
                    self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_details_list[i]))).send_keys(data.Orange_hrm_Data.salary_details_list[i])
                elif locators.Orange_hrm_Locators.salary_details_list[i].endswith('div'):
                    dropdown=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.salary_details_list[i])))
                    self.action.click(dropdown).perform()
                    self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()=" + "'" +data.Orange_hrm_Data.salary_details_list[i]+ "']").click()

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_details_direct_deposit_toggle))).click()
            for i in range(len(locators.Orange_hrm_Locators.salary_deposit_list)):
                if locators.Orange_hrm_Locators.salary_deposit_list[i].endswith('input'):
                    self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_deposit_list[i]))).send_keys(data.Orange_hrm_Data.salary_deposit_list[i])
                elif locators.Orange_hrm_Locators.salary_deposit_list[i].endswith('div'):
                    dropdown=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.salary_deposit_list[i])))
                    self.action.click(dropdown).perform()
                    self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()=" + "'" +data.Orange_hrm_Data.salary_deposit_list[i]+ "']").click()

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_details_save_btn))).click()

            for i in range(len(locators.Orange_hrm_Locators.salary_result)):
                try:
                    info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.salary_result[i]))).text
                    salary_details_result.append(info)
                except Exception as e:
                    print(e)

        except Exception as e:
            print('Cannot be able to validate salary details, error occurred:', e)

        print('data given to the form:', data.Orange_hrm_Data.salary_result)
        print("data present in the form:", salary_details_result)
        print('#--------------###############----------------#')

        if salary_details_result==data.Orange_hrm_Data.salary_result:
            print("Validated salary details successfully")
            assert True
        else:
            print("salary details are invalid")
            assert False

    def test_employee_salary_tax_exemptions(self,booting_function,login):
        salary_tax_exemptions_result=[]
        try:
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

            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.tax_exemptions))).click()
            for i in range(len(locators.Orange_hrm_Locators.tax_exemption_list)):
                if locators.Orange_hrm_Locators.tax_exemption_list[i].endswith('input'):
                    self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.tax_exemption_list[i]))).send_keys(data.Orange_hrm_Data.tax_exemptions_list[i])
                elif locators.Orange_hrm_Locators.tax_exemption_list[i].endswith('div'):
                    dropdown=self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.tax_exemption_list[i])))
                    self.action.click(dropdown).perform()
                    self.driver.find_element(by=By.XPATH, value="//div[@role='listbox']//span[text()=" + "'" +data.Orange_hrm_Data.tax_exemptions_list[i]+ "']").click()
            self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.tax_details_save_btn))).click()

            for i in range(len(locators.Orange_hrm_Locators.tax_exemption_list)):
                try:
                    if locators.Orange_hrm_Locators.tax_exemption_list[i].endswith('input'):
                        info=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.Orange_hrm_Locators.tax_exemption_list[i]))).get_attribute("value")
                        salary_tax_exemptions_result.append(info)
                    elif locators.Orange_hrm_Locators.tax_exemption_list[i].endswith('div'):
                        info = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.Orange_hrm_Locators.tax_exemption_list[i]))).text
                except Exception as e:
                    print(e)

        except Exception as e:
            print('Cannot be able to validate tax exemption details, error occurred:', e)

        print('data given to the form:', data.Orange_hrm_Data.tax_exemptions_list)
        print("data present in the form:", salary_tax_exemptions_result)
        print('#--------------###############----------------#')

        if salary_tax_exemptions_result==data.Orange_hrm_Data.tax_exemptions_list:
            print("Validated tax exemptions details successfully")
            assert True
        else:
            print("tax exemptions are invalid")
            assert False














