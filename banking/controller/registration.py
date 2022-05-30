from flask import render_template

from service.validation import *
from repository.userLogin_dao import *
def get_registration_page():
    return render_template("registration.html")

def register_user(register_input):
    # validate input
    print(register_input)
    username = register_input['username']
    password = register_input['password']
    if validate_registration(username, password):
        # create user
        user_id = insert_user(username, password)
        # info_id = create_user_info(user_id, register_input)
        if user_id is not None:
            return render_template("login.html")
    else:
        return "Failed to register, improper username and password"