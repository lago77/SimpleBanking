class Transactions:

    def __init__ (self, user_id, trans_id, account_id, amount, trans_type):
        self.user_id = user_id
        self.trans_id= trans_id
        self.account_id = account_id
        self.amount = amount
        self.trans_type = trans_type

    def __repr__(self):

        return f"User Info: User id: {self.user_id} || Transaction id: {self.trans_id} ||  Account id: {self.account_id} || Amount: {self.amount} || Transction Type: {self.trans_type}"