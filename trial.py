import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def login(self,booting_function):
        self.driver.get(data.Orange_hrm_Data().url)
        # sleep(5)
        self.wait.until(EC.presence_of_element_located((By.NAME,locators.Orange_hrm_Locators().username_inputBox))).send_keys(data.Orange_hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators().username_inputBox)
        self.driver.find_element(by=By.NAME, value=locators.Orange_hrm_Locators.password_InputBox).send_keys(data.Orange_hrm_Data.password)
        self.driver.find_element(by=By.XPATH, value=locators.Orange_hrm_Locators.LoginButton).click()

def test_validate_dropdown(browser):

    # Find the dropdown element
    dropdown = browser.find_element_by_id("my-dropdown")

    # Create an instance of ActionChains class
    action = ActionChains(browser)

    # Hover over the dropdown element
    action.move_to_element(dropdown).perform()

    # Get all the options in the dropdown
    options = dropdown.find_elements_by_tag_name("option")

    # Loop through the options and validate their contents
    for option in options:
        action.move_to_element(option).perform()

        # Perform your validation logic here
        # For example, assert that the option text is not empty
        assert option.text != ""
