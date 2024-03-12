class Accounts:
    def __init__(self, password, name, dateOfBirth):
        self.password = password 
        self.name = name
        self.dateOfBirth = dateOfBirth

class User(Accounts):
    def __init__(self, password, name, dateOfBirth, employeeNumber, phone):
        super().__init__(password, name, dateOfBirth)
        self.employeeNumber = employeeNumber
        self.phone = phone

    def show_user(self):
        print("----- Employee Profile -----")
        print(f"Name: {self.name}")
        print(f"Employee Number: {self.employeeNumber}")
        print(f"Date of Birth: {self.dateOfBirth}")
        print(f"Phone Number: {self.phone}")

class Admin(Accounts):
  def __init__(self, password, name, dateOfBirth):
    super().__init__(password, name, dateOfBirth)
