class User:

    def __init__ (self, user_id, info_id, first_name, last_name, email, address, phone_number):
        self.user_id = user_id
        self.info_id = info_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number
    def __repr__(self):

        return f"User Info: Info id: {self.info_id} || User id: {self.user_id} || First name: {self.first_name} || Last name: {self.last_name} || Email: {self.email} || Address: {self.address} || Phone number: {self.phone_number}"