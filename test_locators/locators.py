# locators.py - File where all The HTML Locators areKept
class Orange_hrm_Locators:
    username_inputBox = 'username'
    password_InputBox = 'password'
    LoginButton ='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

    invalid_alert = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'

    pim_tab = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    firstname_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    middlename_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    lastname_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    employee_id_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    added_user_toast='//*[@id="oxd-toaster_1"]'

    edit_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]'
    edit_firstname_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    edit_middlename_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    edit_lastname_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    edit_employee_id_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    edit_employee_details_save='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    edit_employee_toast='//*[@id="oxd-toaster_1"]'

    delete_user_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'
    confirm_delete_button='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    deleted_user_toast='//*[@id="oxd-toaster_1"]'



    admin_tab='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    my_info_tab='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
    username_firstname='firstName'
    username_lastname='lastName'
    nickname='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    employee_id='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    other_id='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    license_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    ssn_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    sin_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    nationality_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    marital_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'

    admin_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    leave_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'
    time_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'
    recruitment_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a'
    my_info_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
    performance_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'
    dashboard_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'
    directory_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'
    maintenance_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'
    buzz_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a'

    pim='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    dd='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    menu_options='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul'

    search_bar='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'

    small_tabs = ['admin', 'pim', 'leave', 'time', 'recruitment', 'my info', 'performance', 'dashboard', 'directory',
                  'maintenance', 'buzz']
    def capitalize_list(item):
        return item.upper()
    caps_tabs = list(map(capitalize_list, small_tabs))
    tabs_xpath = [admin_xpath, pim_xpath, leave_xpath, time_xpath, recruitment_xpath, my_info_xpath, performance_xpath,
                  dashboard_xpath, directory_xpath, maintenance_xpath, buzz_xpath]

    # save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'


