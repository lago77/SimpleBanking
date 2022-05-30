from flask import render_template
from flask import redirect, url_for
from repository.userLogin_dao import *
def get_login_page():
    return render_template("login.html")

def check_user_login(login_input):
    # user_login = check_login(login_input)
    print("my login isss")
    myusername=login_input['username']
    id =select_user(myusername).user_id
    print("my id is")
    print(id)
    print(login_input['username'])
    email=''

    return redirect(url_for("account_page",userid=id))