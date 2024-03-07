class Database:
    def __init__(self):
        # Initialize an empty dictionary to store user information
        self.users = {
            "LiamOBrien": {"password": "Python11", "name": "Liam O'Brien", "date_of_birth": "01/01/1988",
                           "employee_num": "00001", "phone": "077330234"},

            "CiaranOBrien": {"password": "Python12", "name": "Ciaran O'Brien", "date_of_birth": "05/05/1976",
                             "employee_num": "00002", "phone": "077234235"},

            "SineadOBrien": {"password": "Python13", "name": "Sinead O'Brien", "date_of_birth": "11/10/1966",
                             "employee_num": "00003", "phone": "077125452"}
        }
        self.admin = {
            "Admin69": {"password": "CSharpisbetter", "name": "Bill Gates", "date_of_birth": "1970-01-01"}
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
