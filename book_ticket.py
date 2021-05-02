
from mysql_connector import *
from tabulate import tabulate;


def book_ticket(user_id):
    while 1:
        
        mycursor = mydb.cursor()
        name=input("\nENTER NAME OF THE PASSENGER: ").strip()
        age=input("\nENTER AGE OF THE PASSENGER: ").strip()
        train=int(input("\nTRAIN NUMBER : "))
        class_type=input("\nEnter class : ").strip()
        mobile=input("\nENTER MOBILE NUMBER: ").strip()

        query="select count(*) from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        myresult = mycursor.fetchone()[0]
        if myresult==0:
           print("\nWrong Train Number - Program aborted")
           return

        ticket_number=1 
        try:
           query="select MAX(ticket_number) from bookings"
           mycursor.execute(query)
           ticket_number = mycursor.fetchone()[0]+1 
        except:
            pass
        
        
        query="select price from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        price = int(mycursor.fetchone()[0])


        query="select source from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        source = (mycursor.fetchone()[0])


        query="select destination from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        destination = (mycursor.fetchone()[0])


        query="select seats from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        seats_remaining= (mycursor.fetchone()[0])

        query="select price from train where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(query)
        fair = (mycursor.fetchone()[0])

        if(seats_remaining<=0):
            print("\nSorry!!! All seats are booked!!!\n")
            return
        
        sql="update train set seats=seats-1 where id="+str(train)+" and class_type="+"'"+class_type+"'"
        mycursor.execute(sql) 
        mydb.commit()
        


        print("\n",source,"--->",destination,"\n")
        print("\nYour ticket number : ",ticket_number)
        print("\nFair to be paid : ₹",fair,"/-",sep='')


        sql = "INSERT INTO bookings (ticket_number,user_id,train_id,source,destination,class_type,price,name,phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (ticket_number,user_id,train,source,destination,class_type,price,name,mobile)
        mycursor.execute(sql, val) 
        mydb.commit()
        print("\nBOOKED SUCCESSFULLY!!!!\n")
        opt=input("\nDo you want to book another train? : y/n : ").strip() 
        if opt!='y':
            return 