from flask import render_template, redirect, url_for
import re
from repository.usertransaction_dao import *
from repository.useraccount_dao import *
def transactions(req):
    print("in the function")
    print("reqs")
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
    return redirect(url_for("processing_transactions",userid=id))





def transaction_page(input):
    print("in deposit form")
    print(input)
    id=input['userid']
        ##get the account id first
    data1=insert_transaction(3,151, "debit")
    data=select_accounts_by_id(6)    
    print("my data")
    print(data1)
    for x in data:
        print("data")
        print(x)
        print(x[0])
       
    mylist=[1,3]
    return render_template("transactions.html", userid=id, list=data)