
from mysql_connector import *

def delete_train():
    
    while 1:
        
        mycursor = mydb.cursor()
        num=int(input("\nEnter train id to be deleted : "))
        clas=input("\nEnter class to be deleted : ").strip() 
        QUERY="delete from train where id="+str(num)+" and class_type='"+clas+"'"
        # print(QUERY)
        mycursor.execute(  QUERY)
        mydb.commit()
        print("\nDeleted From the database!!!\n")
        op=input("\nDo you want to delete any further details? : y/n : ").strip() 
        if op!='y':
            break