from flask import render_template
from flask import redirect, url_for
from repository.userLogin_dao import *
from repository.userInfo_dao import *
from repository.useraccount_dao import *
import re
def get_account(req):
    print("in get_account")
    print("*******************")
    print(req)
    req1="my testing"
    print("my req", req)
    user_info=select_by_user(req)
    print(user_info)
    print("my user")
    data=select_accounts_by_id(req)    
    print("my data")
    print(data)
    for x in data:
        print("data")
        print(x)
        print(x[0])
        print(x[2])
   
        # self.user_id = user_id
        # self.info_id = info_id
        # self.first_name = first_name
        # self.last_name = last_name
        # self.email = email
        # self.address = address
        # self.phone_number = phone_number
    if user_info==None:
        return render_template("accounts.html", userid=req)
    else:
        return render_template("accounts.html", userid=req, firstname=user_info.first_name, lastname=user_info.last_name, email=user_info.email, address=user_info.address, phone=user_info.phone_number, infoid=user_info.info_id, list=data)


def start_profile(input):
    print("my input testing")
    print(input.args)
    dict=input.args
    re_num = re.compile(r'^[0-9]*$')
    id=''
    print("before for loop")
    for x in dict:
        print("start")
        num_conditional = (re_num.search(x)!=None)
        print(x)
        if num_conditional:
            id=int(x)
    # print("my username")
    # print(myusername)
    # print("Start")
    # for x in myusername:
    #     username=x
    # print("my username")
    # print(username)
    print("my id in start profile")
    print("ending")
    return redirect(url_for("start_profiles",userid=id))

def startform(req):
      print("in startform the function")
      print(req)
      re_num = re.compile(r'^[0-9]*$')
      id=''
      print("before for loop")
      for x in req:
        print("start")
        num_conditional = (re_num.search(x)!=None)
        print(x)
        if num_conditional:
            id=int(x)

    #   insert_account(id, balance)
      print("end startform")


      return redirect(url_for("create_account",userid=id))

def account_form(input):
        print(input['userid'])
        print("test")
        id=input['userid']
        print(id)
        print("in accountform")
        print(id)

        return render_template("account_creation.html", userid=id)

def processing_account(input):
    print("in processing account")
    print(input)
    print(input['balance'])
    balance=input['balance']
    re_num = re.compile(r'^[0-9]*$')
    id=''
    print("before for loop")
    for x in input:
        print("start")
        num_conditional = (re_num.search(x)!=None)
        print(x)
        if num_conditional:
            id=int(x)

    insert_account(id, balance)
    print(id)



    return redirect(url_for("account_page",userid=id))

# def profile_form(input):
#     # user_login = check_login(login_input)
#     print("my login isss")
#     myusername=login_input['username']
#     id =select_user(myusername).user_id
#     print("my id is")
#     print(id)
#     print(login_input['username'])

#     return redirect(url_for("profile",userid=id, username=myusername))

