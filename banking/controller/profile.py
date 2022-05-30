from flask import render_template
from repository.userLogin_dao import *
from service.validation import *
from repository.userInfo_dao import *
from flask import redirect, url_for

import re
def starting_profile(input):
    print("my input")
    print(input)
    
    re_num = re.compile(r'^[0-9]*$')
    id=''
    print("before for loop")
    for x in input:
        print("start")
        num_conditional = (re_num.search(x)!=None)
        print(x)
        if num_conditional:
            id=x
    # print("my username")
    # print(myusername)
    # print("Start")
    # for x in myusername:
    #     username=x
    # print("my username")
    # print(username)
    print("end")
    return redirect(url_for("start_form",userid=id))


def start_form(user_id):
    info_id=''
    try:
        account=select_by_user(user_id)
        print("my id")
        print("||||||||||||||||||")
        print(account)
        id=user_id
        print(account.info_id)
        info_id=account.info_id
        print(info_id)
    except(Exception) as e:
        print("error", e)
        pass
    if info_id:
        return render_template("profile_form.html",userid=id, infoid=info_id)
    else:
        info_id=''
        return render_template("profile_form.html",userid=id, infoid=info_id)


def insert_info(input):


# def add_profile(profile_input):
    print("start")

    user_id=''
    for x in input:
        # print("----")
        # print(x)
        # print(type(x))
        re_num = re.compile(r'^[0-9]*$')
        num_conditional = (re_num.search(x)!=None)
        # print(num_conditional)
        if num_conditional:
            user_id=x
        # print("---")

    firstname=input['first_name']
    lastname =input['last_name']
    myemail=input['email']
    myaddress=input['address']
    myphone=input['phone']
    mylist=[1,2,3]
    testuser = select_by_user(user_id)
    if testuser ==None:
        if validate_info(firstname, lastname, myemail, myphone):
            insert_user_info(user_id, firstname, lastname, myemail, myaddress,myphone)
            return redirect(url_for("account_page",userid=user_id))
            # return render_template("accounts.html",userid=user_id,first_name=firstname, last_name = lastname, email=myemail, address=myaddress, phone=myphone, newlist=mylist )
        
        else:
            return "Erroneous user information"
    else:
        update_user_info(user_id, firstname, lastname, myemail, myaddress,myphone)
        return redirect(url_for("account_page",userid=user_id))


# def update_start(input):

#     print(input)
#     print("my input")
#     for x in input:
#         # print("----")
#         # print(x)
#         # print(type(x))
#         re_num = re.compile(r'^[0-9]*$')
#         num_conditional = (re_num.search(x)!=None)
#         # print(num_conditional)
#         if num_conditional:
#             user_id=x
#     # return "test"
#     print("////////////////////")
#     print(user_id)
#     return redirect(url_for("update_user",userid=user_id))


# def update_user_info( req):
#     print("Test")

#     return "Test"