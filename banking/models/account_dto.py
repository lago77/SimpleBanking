class Account:

    def __init__ (self, user_id, account_id, balance):
        self.user_id = user_id
        self.account_id= account_id
        self.balance = balance

    def __repr__(self):

        return f"User Info: User id: {self.user_id} || Account id: {self.account_id} || Balance: {self.balance}"