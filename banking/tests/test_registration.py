
import re
import pytest
@pytest.mark.parametrize("username, password",[('myusername','testffss@'),('notl','mypassword!'), ('username!','mypassword!'), ('user name', 'pass word!')])
def test_validate_registration(username, password):

    # username must be greater than 4 characters. Must contain alphanumeric characters.

    #password must be greater than 6 characters. Can use alphanumeric and non-alphanumeric characters.

    regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search
    # method of regex object.   
    #checks to make sure the password contains atleast one alphanumeric character and is greater than six characters
    password_conditional = (regex.search(password) != None) and (len(password)>6)  and ( " " not in password)
    #check to make sure the username does not contain alphanumeric characters and is greater than or equal to five characters
    username_conditional = (regex.search(username) == None) and (len(username)>=5) and ( " " not in username)

    # password_whitespace=( " " not in password_conditional)


    # if ((regex.search(password) == None) or (len(password)<=6)) or ((regex.search(username) != None) or (len(username)<5)):
    #     print("Passord or username invalid")
    #     print(regex.search(username))
    #     return False
    # else:
    #     print("Password and username valid")
    #     return True
    #     # print(regex.search(mystring))
    #     # # print(len(mystring))
    #     # print(len(mystring)>6)
    #     # print((regex.search(mystring) == None) and (len(mystring)>6))


    assert password_conditional == True, "Password is not atleast 6 characters long or does not have a special character in it and contain no whitespaces"
    assert username_conditional == True, "Username is less than 5 characters or uses non-alphanumeric characters and contain no whitespaces"