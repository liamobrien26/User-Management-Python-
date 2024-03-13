import os
from database import Database
import time
from Account import User, Admin, Accounts
import os
import time
from admin_Menu import AdminMenu
from user_Menu import UserAccounts

def Login(database):
    print("----- LOGIN -----\n")

    # Allow the user three attempts
    for attempt in range(3):
        company_login_user = input("Enter your username: \n")
        company_login_password = input("\nEnter your password: \n")

        # Check if the entered username is in the user database (including both users and admin)
        if company_login_user in database.users or company_login_user in database.admin:
            # Check if the entered password matches the stored password for users
            if company_login_user in database.users:
                account = database.users[company_login_user]
                if account.password == company_login_password:
                    os.system('clear')
                    print("Login successful!")
                    time.sleep(3)
                    os.system('clear')
                    return account  # Return the username if login is successful
            # Check if the entered password matches the stored password for admin
            elif company_login_user in database.admin:
                account = database.admin[company_login_user]
                if account.password == company_login_password:
                    os.system('clear')
                    print("Login successful! (Admin)")
                    time.sleep(3)
                    os.system('clear')
                    return account  # Return the username if login is successful (Admin)
            else:
                os.system('clear')  # Use a different command if not on Windows
                print("Incorrect password. Please try again.")
        else:
            os.system('clear')  # Use a different command if not on Windows
            print(f"Attempt {attempt + 1} - Username does not exist. Please try again.")

    # If all attempts are exhausted
    print("Maximum login attempts reached. Exiting...")


# Create an instance of the Database class
my_database = Database()

# Call the Login function with the created database
logged_in_user = Login(my_database)

# Create an instance of the Database class
user_database = Database()

# Call the register_user function with the database instance
# register_user(user_database)

if (isinstance(logged_in_user, Admin)):
    AdminMenu(my_database,logged_in_user)
else:
    UserAccounts(logged_in_user)  # declares the function for users

"""Print the updated user database
print("Updated User Database:", user_database.users)"""