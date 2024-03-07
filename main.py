import os
from database import Database
import time
from datetime import datetime

import os
import time
def Login(database):
    print("-----HR System-----\n")

    # Allow the user three attempts
    for attempt in range(3):
        company_login_user = input("Enter your username: \n")
        company_login_password = input("Enter your password: \n")

        # Check if the entered username is in the user database (including both users and admin)
        if company_login_user in database.users or company_login_user in database.admin:
            # Check if the entered password matches the stored password for users
            if company_login_user in database.users and database.users[company_login_user]["password"] == company_login_password:
                os.system('clear')
                print("Login successful!")
                time.sleep(3)
                os.system('clear')
                return company_login_user  # Return the username if login is successful
            # Check if the entered password matches the stored password for admin
            elif company_login_user in database.admin and database.admin[company_login_user]["password"] == company_login_password:
                os.system('clear')
                print("Login successful! (Admin)")
                time.sleep(3)
                os.system('clear')
                return company_login_user  # Return the username if login is successful (Admin)
            else:
                os.system('clear')  # Use a different command if not on Windows
                print("Incorrect password. Please try again.")
        else:
            os.system('clear')  # Use a different command if not on Windows
            print(f"Attempt {attempt + 1} - Username does not exist. Please try again.")

    # If all attempts are exhausted
    print("Maximum login attempts reached. Exiting...")


# Function for admin to edit
def register_user(database):
    print("-----HR System-----\n")
    company_register_user = input("Enter username: \n")
    company_register_password = input("Enter password: \n")

    # Save the user information to the database
    database.add_user(company_register_user, company_register_password)
    print("User information saved successfully.\n")

    return company_register_user, company_register_password

def AdminMenu(database, company_login_user):
    print("----- Welcome", database.admin[company_login_user]["name"], "(ADMIN) -----")
    optionAdmin = int(input("1. View all employee profiles\n2. Select Individual Profile\n"
                            "3. Add new Profile\n4. Delete Profile\n\nPlease select an option:"))

    if optionAdmin == 1:  # View all profiles
        print("\nAll Employee Profiles:")
        for username, details in database.users.items():
            print(f"Username: {username}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("\n" + "-" * 30)

    if optionAdmin == 2: #Select individual profile
        print("Please select which employee profile you wish to see")
        # Initialize an empty list to store names
        user_names = []

        # Iterate through the keys in the database.users dictionary and append the 'name' attribute to the list
        for username, user_info in database.users.items():
            user_names.append(user_info['name'])

        # Print the list of names
        print(user_names)

    else:
        print("Invalid option selected.")


def UserAccounts(logged_in_user): #Menu for users
    DisplayUsersName(user_database, logged_in_user)

    # Access the name and date_of_birth using logged_in_user
    user_profile = user_database.users.get(logged_in_user, {})

    optionUser = int(input(
        """1. View your Employee Profile\n2. Edit Your Personal Data\n\nPlease select an option: """))
    os.system('clear')

    if optionUser == 1:  # View Profile

        print("----- Employee Profile -----")
        print(f"Name: {user_profile.get('name')}")
        print(f"Employee Number: {user_profile.get('employee_num')}")
        print(f"Date of Birth: {user_profile.get('date_of_birth')}")
        print(f"Phone Number: {user_profile.get('phone')}")

    elif optionUser == 2:  # Edit personal data
        print("----- Personal Data -----")
        optionEdit = int(input("1. Name\n2. Date of Birth\n3. Phone Number\n4. Username\n5. Password"
                               "\n\nPlease select an option you wish to edit: "))

        if optionEdit == 1:  # Change Name
            os.system('clear')
            current_name = user_profile.get('name')
            print(f"Current Name: {current_name}")
            new_name = input("Please enter the new name you wish to set: ")
            user_profile["name"] = new_name
            os.system('clear')
            updated_name = user_profile.get('name')
            print(f"Updated name: {updated_name}\nYour name has been successfully changed.\nPress Enter to continue.")


        elif optionEdit == 2:  # Change date of birth
            os.system('clear')
            print(f"Date of Birth: {user_profile.get('date_of_birth')}")
            birthday = input("Please enter the new Date of Birth you wish to set in (dd/mm/yyyy) format: ")

            # Convert the inputted date of birth to datetime object
            bday = datetime.strptime(birthday, '%d/%m/%Y')

            # Update the user_profile with the new date of birth
            user_profile["date of birth"] = bday
            os.system('clear')
            updated_DOB = bday.strftime('%d-%m-%Y')  # Sets DOB format
            print(
                f"Updated Date of Birth: {updated_DOB}\nYour Date of Birth has been successfully changed.\n"
                f"Press Enter to continue.")

        elif optionEdit == 3:  # Change phone number
            os.system('clear')
            print(f"Phone Number: {user_profile.get('phone')}")
            phone_number = input("Please enter the new phone number you wish to set: ")
            user_profile['phone'] = phone_number
            os.system('clear')
            updated_phone = user_profile.get('phone')
            print(f"Updated phone number: {updated_phone}\n"
                  f"Your phone number has been successfully changed.\nPress Enter to continue.")


        elif optionEdit == 4:  # Change Username
            os.system('clear')
            print(f"Username: {logged_in_user}")
            user_name = input("Please enter the username you wish to set: ")
            user_profile[logged_in_user] = user_name
            os.system('clear')
            updated_user = user_profile.get(logged_in_user)
            print(f"Updated username: {updated_user}\n"
                  f"Your username has been successfully changed.\nPress Enter to continue.")

        elif optionEdit == 5:  # Change password
            os.system('clear')
            check_password = input("To proceed with the password change, please re-enter your current password: ")
            if check_password == user_profile.get('password'):
                print("ACCESS GRANTED")
                time.sleep(2)
                os.system('clear')
                password = input("Please enter a new password you wish to set: ")
                user_profile['password'] = password
                os.system('clear')
                updated_password = user_profile.get('password')
                print(f"Updated passwordr: {updated_password}\n"
                      f"Your password has been successfully changed.\nPress Enter to continue.")
            else:
                print("Incorrect Password!!")

        else:
            print("Invalid input!")  # optionEdit input falls out of option 1,2,3,4,5


    else:
        print("Invalid input!")  # optionUser input falls outside of option 1 or 2


def DisplayUsersName(database, company_login_user):  # Function for user's name
    print("----- Welcome", database.users[company_login_user]["name"], " -----")

# Create an instance of the Database class
my_database = Database()

# Call the Login function with the created database
logged_in_user = Login(my_database)

# Create an instance of the Database class
user_database = Database()

# Call the register_user function with the database instance
# register_user(user_database)

AdminMenu(my_database,logged_in_user)
UserAccounts(logged_in_user)  # declares the function for users

"""Print the updated user database
print("Updated User Database:", user_database.users)"""