import os
from Account import User, Admin, Accounts
from datetime import datetime
import time


#Page for USERS
def UserAccounts(my_database, company_login_user): 

    print("----- Welcome", company_login_user.name, " -----") #Display welcome sign and name

    optionUser = int(input(
        """1. View your Employee Profile\n2. Edit Your Personal Data\n\nPlease select an option: """))
    os.system('clear')

    if optionUser == 1:  # View Profile

        company_login_user.show_user()

    elif optionUser == 2:  # Edit personal data
        print("----- Personal Data -----")
        optionEdit = int(input("1. Name\n2. Date of Birth\n3. Phone Number\n4. Username\n5. Password"
                               "\n\nPlease select an option you wish to edit: "))

        if optionEdit == 1:  # Change Name
            os.system('clear')
            current_name = company_login_user.name
            print("----- CHANGE NAME -----")
            print(f"Current Name: {current_name}")
            new_name = input("\nPlease enter the new name you wish to set: ")
            company_login_user.name= new_name
            os.system('clear')
            print(f"Updated name: {company_login_user.name}\n\nYour name has been successfully changed.\n\nPress Enter to continue.")

        elif optionEdit == 2:  # Change date of birth
            os.system('clear')
            print(f"Date of Birth: {company_login_user.dateOfBirth}")
            birthday = input("Please enter the new Date of Birth you wish to set in (dd/mm/yyyy) format: ")
            # Convert the inputted date of birth to datetime object
            bday = datetime.strptime(birthday, '%d/%m/%Y')

            # Update the user_profile with the new date of birth
            company_login_user.dateOfBirth = bday
            os.system('clear')
            updated_DOB = bday.strftime('%d-%m-%Y')  # Sets DOB format
            print(
                f"Updated Date of Birth: {updated_DOB}\nYour Date of Birth has been successfully changed.\n"
                f"Press Enter to continue.")

        elif optionEdit == 3:  # Change phone number
            os.system('clear')
            print(f"Phone Number: {company_login_user.phone}")
            phone_number = input("Please enter the new phone number you wish to set: ")
            company_login_user.phone = phone_number
            os.system('clear')
            print(f"Updated phone number: {company_login_user.phone}\n"
                  f"Your phone number has been successfully changed.\nPress Enter to continue.")


        elif optionEdit == 4:  # Change Username
            os.system('clear')
            print(f"Username: {company_login_user.username}")
            user_name = input("Please enter the username you wish to set: ")

            amended_user = my_database.users.pop(company_login_user.username)
            amended_user.username = user_name #Update username in values (dictionary)
            my_database.users[user_name] = amended_user

            os.system('clear')
            print(f"Updated username: {company_login_user.username}\n"
                  f"Your username has been successfully changed.\nPress Enter to continue.")

        elif optionEdit == 5:  # Change password
            os.system('clear')
            check_password = input("To proceed with the password change, please re-enter your current password: ")
            if check_password == company_login_user.password:
                print("ACCESS GRANTED")
                time.sleep(2)
                os.system('clear')
                password = input("Please enter a new password you wish to set: ")
                company_login_user.password = password
                os.system('clear')
                print(f"Updated passwordr: {company_login_user.password}\n"
                      f"Your password has been successfully changed.\nPress Enter to continue.")
            else:
                print("Incorrect Password!!")

        else:
            print("Invalid input!")  # optionEdit input falls out of option 1,2,3,4,5



    else:
        print("Invalid input!")  # optionUser input falls outside of option 1 or 2