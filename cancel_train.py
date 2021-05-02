from mysql_connector import *



def cancel_train(user_id,train_id,class_type):
    
    mycursor = mydb.cursor()
    ticket_number=input("\nEnter ticket number : ")
    query="select count(*) from bookings where train_id="+str(train_id)+" and class_type="+"'"+class_type+"'"+" and user_id='"+str(user_id)+"'"+" and ticket_number="+ticket_number
    mycursor.execute(query)
    myresult = mycursor.fetchone()[0]
    if myresult==0:
        print("\nWrong Train Number  - Program aborted\n")
        return
    query="delete from bookings where train_id="+str(train_id)+" and class_type="+"'"+class_type+"'"+" and user_id='"+str(user_id)+"'"+" and ticket_number="+ticket_number
     


    sql="update train set seats=seats+1 where id="+str(train_id)+" and class_type="+"'"+class_type+"'"
    mycursor.execute(sql) 
    mydb.commit()

    
    mycursor.execute(query)
    print("\nYour booking has been cancelled successfully!!!\n")
    mydb.commit()
    