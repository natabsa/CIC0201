
from client import User

class AuthenticationService:
    
    users = [
        User("user", ""),
        User("john", ""),
        User("jane", ""),
        User("bob", ""),
        User("alice", ""),
        User("charlie", ""),
        User("diana", ""),
        User("lucca", ""),
        User("chris", ""),
        User("tony", ""),
        User("carm", ""),
        User("meg", "")
    ]

    def __init__(self):
        return
    
    def authenticate(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False
    
    

