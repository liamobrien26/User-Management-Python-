import os
from database import Database
from Account import User, Admin, Accounts



#Page for admin


def AdminMenu(database, company_login_user):
    print("----- Welcome", company_login_user.name, "(ADMIN) -----")
    optionAdmin = int(input("1. View all employee profiles\n2. Select Individual Profile\n"
                            "3. Add new Profile\n4. Delete Profile\n\nPlease select an option:"))

    if optionAdmin == 1:  # View all profiles
        os.system('clear')
        print("\n--- All Employee Profiles ---\n\n")

        
       
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



def register_user(database):
    print("-----HR System-----\n")
    company_register_user = input("Enter username: \n")
    company_register_password = input("Enter password: \n")

    # Save the user information to the database
    database.add_user(company_register_user, company_register_password)
    print("User information saved successfully.\n")

    return company_register_user, company_register_password