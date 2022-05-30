import re

def validate_balance(balance):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    balance_conditional_isnum= ((isinstance(balance,float) or isinstance(balance,int)))
    
    balance_conditional_ispositive =  (balance>=0)

    return (balance_conditional_isnum and balance_conditional_ispositive)

def validate_info(first_name, last_name, email, phone_number):


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

    return (first_name_conditional and last_name_conditional and email_conditional and phone_conditional)

def validate_registration(username, password):

    # username must be greater than 4 characters. Must contain alphanumeric characters.

    #password must be greater than 6 characters. Can use alphanumeric and non-alphanumeric characters.

    regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
     
    # Pass the string in search
    # method of regex object.   
    #checks to make sure the password contains atleast one alphanumeric character and is greater than six characters
    password_conditional = (regex.search(password) != None) and (len(password)>6)  and ( " " not in password)
    #check to make sure the username does not contain alphanumeric characters and is greater than or equal to five characters
    username_conditional = (regex.search(username) == None) and (len(username)>=5) and ( " " not in username)

    return (username_conditional and password_conditional)

def validate_transfer(amount):
    ##this function tests to make sure the balance is not negative or and not a string when entered.

    amount_conditional_isnum= ((isinstance(amount,float) or isinstance(amount,int)))
    
    amount_conditional_greaterthanzero =  (amount>0)


    return (amount_conditional_greaterthanzero and amount_conditional_greaterthanzero)
