class Accounts:
    def __init__(self, username, password, name, dateOfBirth):
        self.username = username
        self.password = password 
        self.name = name
        self.dateOfBirth = dateOfBirth

class User(Accounts):
    def __init__(self, username, password, name, dateOfBirth, employeeNumber, phone):
        super().__init__(username, password, name, dateOfBirth)
        self.employeeNumber = employeeNumber
        self.phone = phone

    def show_user(self):
        print("----- Employee Profile -----")
        print(f"Name: {self.name}")
        print(f"Employee Number: {self.employeeNumber}")
        print(f"Date of Birth: {self.dateOfBirth}")
        print(f"Phone Number: {self.phone}\n\n")

    def __repr__(self):
        object = "----- Employee Profile -----\n"
        object += "Username: " + self.username + "\n"
        object += "Password: " + self.password + "\n"
        object += "Name: " + self.name + "\n"
        object += "Employee Number: " + self.employeeNumber + "\n"
        object += "Date of Birth: " + self.dateOfBirth + "\n"
        object += "Phone Number: " + self.phone + "\n"
        return object

class Admin(Accounts):
  def __init__(self, username, password, name, dateOfBirth):
    super().__init__(username, password, name, dateOfBirth)

    def __repr__(self):
        object = "----- Admin Profile -----\n"
        object += "Username: " + self.username + "\n"
        object += "Password: " + self.password + "\n"
        object += "Name: " + self.name + "\n"
        object += "Date of Birth: " + self.dateOfBirth + "\n"
        return object
