
from mysql_connector import *
from tabulate import tabulate;




def view_bookings():
    

    mycursor = mydb.cursor()
    print("\n")
    mycursor.execute("SELECT ticket_number,name,user_id,train_id,source,destination,class_type,price,phone FROM  bookings")
    result = mycursor.fetchall()
    header=["TICKET NUMBER","NAME","USER ID","TRAIN NUMBER","FROM","TO","CLASS","PRICE(Rs.)","PHONE"]
    ans=[]
    for i in result:
        ans.append(list(i))
    print(tabulate(ans,headers=header))
    s=input()
    print("\n")