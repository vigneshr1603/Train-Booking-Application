
from mysql_connector import *
from user_options import *;

def new_user():
    
    mycursor = mydb.cursor()
    # getting details
    username = input("Enter username : ").strip()
    email = input("Enter email-id : ").strip()
    password = input("Enter password : ").strip()

    # ----------- to generate unique id --------------------------
    mycursor.execute("SELECT MAX(id) FROM user")
    result = mycursor.fetchall()
    user_id = 0
    for i in result:
        try:
            user_id = int(i[0])+1
            break
        except:
            user_id = 1

    # inserting to data base
    sql = "INSERT INTO user (username,password,emailid,id) VALUES (%s, %s, %s,%s)"
    val = (username, password, email, user_id)
    mycursor.execute(sql, val)
    mydb.commit()

    print("You are now logged in as USER\n")
    user_options(user_id)
