class Login:

    def __init__ (self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
       
    def __repr__(self):

        return f"User Info: User id: {self.user_id} || Username: {self.username} || password: {self.password} ||"