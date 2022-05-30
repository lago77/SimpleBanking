from models.user_info_dto import User
from models.login_dto import Login
from repository.userLogin_dao import insert_user, delete_user, update_password
from repository.userInfo_dao import *
from repository.useraccount_dao import insert_account, update_balance
from repository.usertransaction_dao import *
User_1 = User(1,1,"my", "name", "me@yahoo.ca", "22 address", 43543543)
login_1 = Login(1, "user", "pass")
import re

# delete_user("Abdi", "mypassword1")
#insert_user_info(6, 'Omar', 'Abdi','myemail@yahoo.ca','dfassf street',55654 )
# print(select_user_info_by_id(1).first_name)
# update_password(6, "newpass3")
# print(update_user_info(6, "Omar222", "Abdi22223", "newmail@protonmail.com", "22 street", 555))
# insert_transaction(1,20, "Debit")
mystring ="testingstring"

# insert_account(6, 1000)
# print(User_1)
# print(login_1)
# update_balance(1, 500)
# re_num = re.compile(r'^[^0-9]+$')
# # print(regex.search("mystring"))

# re_spec= re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
###test to make sure the first and last names are not blanks and only contain strings, no numbers and no alphanumerics

# first_name_conditional = (re_num.search(first_name) == None) and ( re_spec.search(first_name) == None)and (len(first_name)>=5) and ( " " not in first_name)
# mystring="sfds@"
# print(re_num.search(mystring)!= None)
# print(re_spec.search(mystring)== None)
num = "165"
re_phone_num = re.compile(r'^[0-9]*$')
# print(re_phone_num.search(num))

re_num= re.compile(r'[a-zA-Z]+')
## pattern that checks for special characters
re_spec= re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
###test to make sure the first and last names are not blanks and only contain strings, no numbers and no alphanumerics

#pattern that checks if an email address is valid
re_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
# re_email.search(email)
first_name="fsfsf"
# first_name_conditional = (re_num.search(first_name)!= None) and ( re_spec.search(first_name) == None) and ( " " not in first_name)
# print(re_spec.search(first_name)== None)


# arr_char = [not char.isdigit() for char in first_name]

# print(arr_char)
# print(all([not char.isdigit() for char in first_name]))
# re_balance = re.compile(r'^[0-9]*$')
# balance_conditional = (re_balance.search(balance)!=None)

balance= 5.012
print("balance is")
print(isinstance(balance, int))
print(isinstance(balance,float))

print(round(balance,2))