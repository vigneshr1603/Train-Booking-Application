import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # <-- change the username here
    password="password",    # <---- change the password here
)
mycursor = mydb.cursor()

# creating database
try:
    mycursor.execute("CREATE DATABASE train_booking_application")
except:
    mycursor.execute("DROP DATABASE train_booking_application")
    mycursor.execute("CREATE DATABASE train_booking_application")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="train_booking_application"

)
mycursor = mydb.cursor()


# admin table
mycursor.execute(
    "CREATE TABLE admin (username VARCHAR(45),password VARCHAR(45))")
mycursor.execute(
    "INSERT INTO admin (username,password) VALUES (%s, %s)", ("admin", "admin"))
mydb.commit()


# user table
mycursor.execute(
    "CREATE TABLE user (id INT,username VARCHAR(45), emailid VARCHAR(45), password VARCHAR(45))")


# train details table
mycursor.execute(
    "CREATE TABLE train (id INT, source VARCHAR(45), destination VARCHAR(45), class_type VARCHAR(5), price INT,seats INT)")


# booking details table
mycursor.execute("CREATE TABLE bookings (ticket_number INT,user_id INT, train_id INT,source VARCHAR(100), destination VARCHAR(100), class_type VARCHAR(5), price INT,name VARCHAR(45), phone VARCHAR(11))")
