from flask import render_template
from flask import redirect, url_for
import re
from repository.usertransaction_dao import *
from repository.useraccount_dao import *
def starting_deposit(req):

    print("starting deposit")
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
    return redirect(url_for("depositing_amount",userid=id))


def deposit_form(input):
    print("in deposit form")
    print(input)
    id=input['userid']
    data=select_accounts_by_id(id)     
    mylist=[1,3]
    return render_template("deposit.html", userid=id, list=data)

def debit(req,input):
    re_num = re.compile(r'^[0-9]*$')
    id=''
    print("in debit")
    print("before for loop")
    # print(input)
    print("checking input")
    print(input)
    for x in input:
        print("start")
        num_conditional = (re_num.search(x)!=None)
        print(x)
        if num_conditional:
            id=int(x)
    print("account")
    print(input['account'])
    account_id=input['account']
    print("amount")
    print(input['amount'])
    amount=input['amount']
    accounts=select_accounts_by_account_id(account_id)
    print("******************************")
    print("my accounts")
    print(accounts)
    balance=accounts[2]
    print(type(amount))
    newbalance = balance + int(amount)

    insert_transaction(id,account_id, amount, "Credit")
    update_balance(account_id, newbalance)
    
    return redirect(url_for("account_page",userid=id))