from flask import Flask, render_template, request
from controller.profile import *

from models.login_dto import Login
from controller.home import *
from controller.login import *
from controller.registration import *
from controller.profile import *
from controller.accounts import *
from controller.transactions import *
from controller.deposit import *
from controller.withdraw import *
from controller.transactions import *
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home_page():
    return get_homepage()

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input/', methods=["POST"])
def user_login():
    print("my request")
    print(request)
    return check_user_login(request.form)
# @app.route('/login/input', methods=["POST"])
# def user_login():
#     return check_user_login(request.form)

@app.route('/registration')
def registration_page():
    return get_registration_page()

@app.route('/registration/input', methods=["POST"])
def registrating_page():
    print("my request")
    print(request.form)
    return register_user(request.form)



@app.route('/profile/create', methods=["POST"])
def get_profile_page():
    print("my form request ||||||||||||||||||||||")
    print(request.form)
    return insert_info(request.form)

@app.route('/accounts/input/', methods=["GET"])
def start_profile_form():
    print("in accounts input")
    print("account startss")
    print(request)
    print(request.args)
    return start_profile(request)

@app.route('/profile', methods=["GET"])
def start_profiles():
    print("my form request")
    print(request.args['userid'])
    return start_form(request.args['userid'])

@app.route('/accounts', methods=["GET", "POST"])
def account_page():
    print("the reuest")
    print(request.args['userid'])
    print("request form")
    print(request.form)
    return get_account(request.args['userid'])

@app.route('/account/create', methods=["GET"])
def starting_form():
    print("in starting_from")
    # print(request.query_string)
    print(request.args)
    return startform(request.args)

@app.route('/account/form', methods=["GET"])
def create_account():
    print("account form")
    print(request.args)
    return account_form(request.args)

@app.route('/account/creation', methods=["POST"])
def initializing_account():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("in account/creation")
    # print(request.query_string)
    print(request.form)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    return processing_account(request.form)

@app.route('/deposit/start', methods=["GET"])
def deposit_start():
    
    print("in deposit_start")
    print(request.args)
    
    return starting_deposit(request.args)

@app.route('/deposit', methods=[ "GET"])
def depositing_amount():
    return deposit_form(request.args)

@app.route('/deposit/debit/', methods=["POST", "GET"])
def process_deposit():
    
    print("in process_deposit")
    print("request")
    print(request.method)
    print(request.args)
    print(request.form)
    return debit(request.args,request.form)

######withdraw

@app.route('/withdraw/start', methods=["GET"])
def withdraw_start():
    print("-=------------------")
    print("in deposit_start")
    print(request.args)
    return starting_withdraw(request.args)

@app.route('/withdraw', methods=[ "GET"])
def withdrawing_amount():
    return withdraw_form(request.args)

@app.route('/withdraw/debit/', methods=["POST", "GET"])
def process_withdraw():
    
    print("in process_deposit")
    print("request")
    print(request.method)
    print(request.args)
    print(request.form)
    return credit(request.args,request.form)

# @app.route('/registration/register', methods=["POST"])
# def register_new_user():
#     return register_user(request.form)
###

@app.route('/transactions/', methods=["POST", "GET"])
def get_transactions():
    print("in transactions/")
    print(request.args)
    print("starting transactions()")
    return transactions(request.args)

@app.route('/transactions/process', methods=["POST", "GET"])   
def processing_transactions():
    
    return transaction_page(request.args)

# @app.route('/update/start', methods=["POST", "GET"])   
# def start_update():
    
#     return update_start(request.args)

@app.route('/update/user', methods=["GET"])   
def update_user():
    print("update requests")
    print(request)
    return update_user_info(request)

@app.route('/close', methods=["GET"])   
def closing_account():
    print("closing account")
    print(request.args)
    return close_account(request.args)


# @app.route('/account/delete', methods=["GET"])   
# def deleting_account():
#     print("closing account")
#     print(request.args)
#     return delete_account(request.args)

# @app.route('/account/delete', methods=["GET"])   
# def delete_accounts():
#     print("closing account")
#     print(request.args)
#     return account_delete_form(request.args)

@app.route('/account/delete', methods=["GET"])
def starting_form_delete():
    print("in starting_from")
    # print(request.query_string)
    print(request.args)
    return startform_delete(request.args)

@app.route('/account/form/delete', methods=["GET"])
def delete_account():
    print("account form")
    print(request.args)
    return account_form_delete(request.args)

@app.route('/account/deletion', methods=["POST"])
def processing_account_deletion():
    print("in account/creation")
    # print(request.query_string)
    print(request.form)
    return deleting_account(request.form)

if __name__ == "__main__":
    app.run(debug=True)