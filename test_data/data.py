# data.py - Keep all your Testing Data in this file
class Orange_hrm_Data:
    url ='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'

    invalid_username='Admin'
    invalid_password='Invalid password'

    test_first_name='Sathish'
    test_middle_name='R'
    test_last_name='Kumar'
    test_employee_id=1260

    user_role_expected_options=['Admin','ESS']
    status_expected_options=['Enabled','Disabled']

    test_login_username='sathishkumar'
    test_login_password='Sathish@123'

    test_first_name1 = 'Sathishkumar'
    test_last_name1 = 'Kumar'
    test_employee_id1 = 12600
    test_login_username1 = 'sathish'
    test_login_password1 = 'Sparkzz@123'



    test_personal_details={'first_name':'Demo_first_name',
          'middle_name' : 'Demo_middle_name',
          'last_name':'Demo_last_name',
          'employee_id':'12345',
          'nick_name': 'Demo_nickname',
          'other_id': '342424235',
          'license_no': '131313knhghjhj7',
          'license_expiry_date': '2040-01-01',
          'ssn_no': '132536',
          'sin_no': '57389579',
          'military_service':'NIL',
          'dob':'2000-05-16',
          'nationality':'Indian',
          'marital_status':'Single'

    }
    contact_details = {'street1': 'uzumaki street',
                             'street2': 'naruto street',
                             'city': 'konahakure',
                             'state': 'land of fire',
                             'zip_code': '600000',
                             'home_no': '1234567',
                             'mobile_no': '9897867575',
                             'work_no': '79797867575',
                             'work_email': 'hokage@mail.com',
                             'other_email': 'uzumaki_naruto@mail.com',
                       }

    personal_details_list=[test_personal_details['first_name'],test_personal_details['middle_name'],test_personal_details['last_name'],test_personal_details['nick_name']
                           ,test_personal_details['employee_id'],test_personal_details['other_id'],test_personal_details['license_no'],test_personal_details['license_expiry_date'],test_personal_details['ssn_no']
                           ,test_personal_details['sin_no'],test_personal_details['dob'],test_personal_details['military_service']]
    contact_details_list=[contact_details['street1'], contact_details['street2'], contact_details['city'], contact_details['state']
                                    , contact_details['zip_code'], contact_details['home_no'], contact_details['mobile_no'], contact_details['work_no'],
                          contact_details['work_email'], contact_details['other_email']]


    # test_username='sathishsparkzz'
    # test_password='Sparkzz@123'


