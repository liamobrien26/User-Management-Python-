from Account import User, Admin

class Database:
    def __init__(self):
        self.users = {
            "LiamOBrien": User("Python11", "Liam O'Brien", "01/01/1988", "00001", "077330234"),

            "CiaranOBrien": User("Python12", "Ciaran O'Brien", "05/05/1976", "00002", "077234235"),

            "SineadOBrien": User("Python13", "Sinead O'Brien", "11/10/1966", "00003", "077125452")
        }
        self.admin = {
            "Admin100": Admin("SixApples6", "Bill Gates", "1970-01-01")
        }

    def add_user(self, username, password, is_admin=False):
        # This method is responsible for adding a new user to the database.
        # The key is the username, and the value is the password

        # Check if the user is an admin
        def add_user(self, username, password):
            if username in self.admins:
                print(f"{username} is an admin. User not added.")
            else:
                self.users[username] = password
                print(f"User {username} added successfully.")
