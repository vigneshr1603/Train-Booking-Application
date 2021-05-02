from tabulate import tabulate

from mysql_connector import *




def view_my_bookings(user_id):
    mycursor = mydb.cursor()
    print("\n")
    mycursor.execute("SELECT ticket_number,name,train_id,source,destination,class_type,price,phone FROM  bookings where user_id="+str(user_id))
    result = mycursor.fetchall()
    ans=[]
    header=["TICKET NUMBER","NAME","TRAIN NUMBER","FROM","TO","CLASS","PRICE(Rs.)","PHONE NUMBER"]
    for i in result:
        ans.append(list(i))
    print(tabulate(ans,headers=header))
    s=input()
    print("\n")