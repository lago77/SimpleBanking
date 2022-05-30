
import re
import pytest
@pytest.mark.parametrize("first_name, last_name, email, phone_number",[("omar", "abdi", "omar@yahoo.com","4554674"),

 ("Abdi ", "abdi", "omar@yahoo.com","4554674"),
 
 ("omar1", "abdi", "omar@yahoo.com","4554674"),
 ("omar", "abdi", "omaryahoo.com","4554674"),
 ("omar", "abdi", "omar@yahoo.com","455464"),
 ("omar", "abdi", "omar@y","4554674")
 
 ])
def test_validate_info(first_name, last_name, email, phone_number):


    ## pattern for matching a string without numbers
    re_num= re.compile(r'/^\d+$/')
    ## pattern that checks for special characters
    re_spec= re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
    ###test to make sure the first and last names are not blanks and only contain strings, no numbers and no alphanumerics

    #pattern that checks if an email address is valid
    re_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    re_email.search(email)

    first_name_conditional = (all([not char.isdigit() for char in first_name])) and ( re_spec.search(first_name) == None) and ( " " not in first_name)
    last_name_conditional = (all([not char.isdigit() for char in last_name])) and ( re_spec.search(last_name) == None) and ( " " not in last_name)

    email_conditional =( re_email.search(email) != None) 

    #tests to see if phone number is a number

    re_phone_num = re.compile(r'^[0-9]*$')
    phone_conditional = (re_phone_num.search(phone_number)!=None) and ((len(phone_number)==7))


    assert first_name_conditional == True, "The first name must not contain numbers or a white space"
    assert last_name_conditional == True, "The last name must not contain numbers or a white space"
    assert email_conditional == True, "Not a valid email"
    assert phone_conditional == True, "Not a valid phone number"