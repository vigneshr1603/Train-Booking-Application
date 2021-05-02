from existing_user import *
from new_user import *
from admin_options import *
from mysql_connector import *

while True:


    
    mycursor = mydb.cursor()
    type_of_user = input("Login as user/admin : u/a : ").strip()

    if type_of_user == "a":

        # for admin
        login_id = input("\nEnter login id : ").strip()
        password = input("Enter password : ").strip()

        mycursor.execute("SELECT * FROM admin")

        details = mycursor.fetchall()

        for i, j in details:
            if i == login_id and j == password:
                print("\nYou are now logged in as ADMIN\n")
                try:
                    admin_options()
                except:
                    print("\nPlease enter correct field values....Logged out.....\n")
                    quit()
                break
        else:
            print("\nWrong Credentials\n")

    elif type_of_user == 'u':

        # for user
        user = input("\nDo you have an existing account y/n? : ").strip().lower()
        try:
            if user == 'y':
                 existing_user()
            elif user == 'n':
                 new_user()
            else:
                 break
        except:
            print("\nPlease enter correct field values....Logged out.....\n")
            quit()
    else:
        break
