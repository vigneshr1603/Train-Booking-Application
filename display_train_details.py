
from mysql_connector import *
from tabulate import tabulate;



def display_train_details():
    
    mycursor = mydb.cursor()
    print("\n")
    mycursor.execute("SELECT id,source,destination,class_type,price FROM train")
    result = mycursor.fetchall()
    header=["TRAIN NUMBER","SOURCE","DESTINATION","CLASS","FAIR(Rs.)"]
    ans=[]
    for i in result:
        ans.append(i)
    print(tabulate(ans,headers=header))
    
    s=input()
    print("\n")