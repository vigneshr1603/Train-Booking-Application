
from user_options import *
from mysql_connector import *

def existing_user():
    
    mycursor = mydb.cursor()
    login_id = input("Enter login id : ").strip()
    password = input("Enter password : ").strip()

    mycursor.execute("SELECT * FROM user")

    details = mycursor.fetchall()

    # checking for user in database
    for k1, i, k, j in details:
        if i == login_id and j == password:
            print("\nYou are now logged in as USER\n")

            user_options(k1)
            break

    else:
        print("\nWrong Credentials\n")
        return
