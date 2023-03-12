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

    login_username_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    login_status_radio='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label'
    login_password_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    login_password_confirm_textbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    login_save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
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

    admin_xpath = "//span[text()='Admin']"
    pim_xpath = "//span[text()='PIM']"
    leave_xpath = "//span[text()='Leave']"
    time_xpath = "//span[text()='Time']"
    recruitment_xpath = "//span[text()='Recruitment']"
    my_info_xpath = "//span[text()='My Info']"
    performance_xpath = "//span[text()='Performance']"
    dashboard_xpath = "//span[text()='Dashboard']"
    directory_xpath = "//span[text()='Directory']"
    maintenance_xpath = "//span[text()='Maintenance']"
    buzz_xpath = "//span[text()='Buzz']"

    login_details_toggle='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label'
    user_management_dropdown='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
    users_option='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li'

    user_role_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div'
    status_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div'


    pim='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'
    dd='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    menu_options='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul'

    search_bar='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'

    small_tabs = ['admin', 'pim', 'leave', 'time', 'recruitment', 'my info', 'performance', 'dashboard', 'directory',
                  'maintenance', 'buzz']

    personal_details='//a[text()="Personal Details"]'
    contact_details = '//a[text()="Contact Details"]'
    emergency_contacts = '//a[text()="Emergency Contacts"]'
    dependants = '//a[text()="Dependents"]'
    immigration = '//a[text()="Immigration"]'
    job = '//a[text()="Job"]'
    salary = '//a[text()="Salary"]'
    tax_exemptions = '//a[text()="Tax Exemptions"]'
    report_to = '//a[text()="Report-to"]'
    qualifications = '//a[text()="Qualifications"]'
    membership = '//a[text()="Memberships"]'

    employee_details_xpath=[personal_details,contact_details,emergency_contacts,dependants,immigration,
                      job,salary,tax_exemptions,report_to,qualifications,membership]
    employee_details = ['personal_details', 'contact_details', 'emergency_contacts', 'dependants', 'immigration',
                        'job', 'salary', 'tax_exemptions', 'report_to', 'qualifications', 'membership']

    def capitalize_list(item):
        return item.upper()
    caps_tabs = list(map(capitalize_list, small_tabs))
    tabs_xpath = [admin_xpath, pim_xpath, leave_xpath, time_xpath, recruitment_xpath, my_info_xpath, performance_xpath,
                  dashboard_xpath, directory_xpath, maintenance_xpath, buzz_xpath]

    personal_details_heading='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6'
    personal_details_first_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    personal_details_middle_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    personal_details_last_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    personal_details_nick_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    personal_details_employee_id_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    personal_details_other_id_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    personal_details_driving_license_no_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    personal_details_license_expiry_date_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    personal_details_ssn_no_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    personal_details_sin_no_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    personal_details_gender_male='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label'
    personal_details_military_service='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    personal_details_dob='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'

    personal_details_nationality='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div'
    personal_details_marital_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'

    personal_details_save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

    personal_details_xpath_list=[personal_details_first_name_xpath,personal_details_middle_name_xpath,personal_details_last_name_xpath,personal_details_nick_name_xpath,
                                 personal_details_employee_id_xpath,personal_details_other_id_xpath,personal_details_driving_license_no_xpath,personal_details_license_expiry_date_xpath,
                                 personal_details_ssn_no_xpath,personal_details_sin_no_xpath,personal_details_dob,personal_details_military_service,]

    contacts_details_street1_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    contacts_details_street2_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    contacts_details_city_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    contacts_details_state_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    contacts_details_zip_code_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    contacts_details_country_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
    contacts_details_home_no_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    contacts_details_mobile_no_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    contacts_details_work_no_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    contacts_details_work_email_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    contacts_details_other_email_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input'

    contacts_details_save_btn_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'

    contacts_details_xpath_list=[contacts_details_street1_xpath, contacts_details_street2_xpath, contacts_details_city_xpath, contacts_details_state_xpath,
                                           contacts_details_zip_code_xpath, contacts_details_home_no_xpath, contacts_details_mobile_no_xpath,
                                           contacts_details_work_no_xpath, contacts_details_work_email_xpath, contacts_details_other_email_xpath]

    emergency_contacts_add_btn_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    emergency_contacts_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    emergency_contacts_relationship_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    emergency_contacts_home_telephone_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    emergency_contacts_mobile_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    emergency_contacts_work_telephone_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    emergency_contacts_save_btn_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    emergency_contacts_name_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    emergency_contacts_relationship_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    emergency_contacts_home_telephone_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'
    emergency_contacts_mobile_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div'
    emergency_contacts_work_telephone_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div'

    emergency_contacts_result_list=[emergency_contacts_name_result,emergency_contacts_relationship_result,emergency_contacts_home_telephone_result,
                                    emergency_contacts_mobile_result,emergency_contacts_work_telephone_result]

    emergency_contacts_xpath_list=[emergency_contacts_name_xpath,emergency_contacts_relationship_xpath,emergency_contacts_home_telephone_xpath,
                                   emergency_contacts_mobile_xpath,emergency_contacts_work_telephone_xpath]


    dependants_name_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    dependants_relationship_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    dependants_dob_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    dependants_add_btn_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    dependants_save_btn_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    dependants_name_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    dependants_relationship_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    dependants_dob_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'

    dependants_xpath_list=[dependants_name_xpath,dependants_relationship_xpath,dependants_dob_xpath]
    dependants_result_list=[dependants_name_result,dependants_relationship_result,dependants_dob_result]

    job_details_joined_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    job_details_job_title_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    job_details_job_specification='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div'
    job_details_job_category_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    job_details_sub_unit_dropdown= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div'
    job_details_location_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
    job_details_employment_status_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div'
    job_details_include_toggle='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label'
    job_details_contract_start_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
    job_details_contract_end_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    job_details_save_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'

    job_details_list=[job_details_joined_date,job_details_job_title_dropdown,job_details_job_specification,job_details_job_category_dropdown,
                      job_details_sub_unit_dropdown,job_details_location_dropdown,job_details_employment_status_dropdown,
                      job_details_include_toggle,job_details_contract_start_date,job_details_contract_end_date]

    job_details_terminate_employee='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    job_details_termination_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'
    job_details_termination_reason_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div'
    job_details_termination_save_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[2]'
    job_details_activate_employee_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button'
    job_details_termination_date_result='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p'

    salary_details_add_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    salary_details_salary_component='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    salary_details_pay_grade_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div'
    salary_details_pay_frequency_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div'
    salary_details_currency_dropdown='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div'
    salary_details_amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    salary_details_direct_deposit_toggle='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label'
    salary_details_save_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[2]'
    salary_details_deposit_account_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    salary_details_deposit_account_type='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div'
    salary_details_deposit_routing_number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    salary_details_deposit_amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'

    salary_details_list=[salary_details_salary_component,salary_details_pay_grade_dropdown,salary_details_pay_frequency_dropdown,salary_details_currency_dropdown,
                         salary_details_amount]

    salary_deposit_list=[salary_details_deposit_account_number,salary_details_deposit_account_type,salary_details_deposit_routing_number,salary_details_deposit_amount]

    salary_component_result = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    salary_amount_result = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    salary_currency_result = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'
    salary_frequency_result = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div'
    salary_deposit_amount = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div'

    salary_result=[salary_component_result,salary_amount_result,salary_currency_result,salary_frequency_result,salary_deposit_amount]

    tax_exemptions_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div'
    tax_exemption='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    tax_exemptions_state_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div'
    tax_state_exemption='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    tax_state_unemployment='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div'
    tax_state_work_state='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div'
    tax_details_save_btn='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button'

    tax_exemption_list=[tax_exemptions_status,tax_exemption,tax_exemptions_state_status,tax_state_exemption,
                        tax_state_unemployment,tax_state_work_state,tax_details_save_btn]





    # save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'


