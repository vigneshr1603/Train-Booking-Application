from mysql_connector import *


def add_train_details():

    mycursor = mydb.cursor()

    # getting input
    while 1:
        source = input("Enter train source: ").strip()
        destination = input("\nEnter train destination: ").strip()
        mycursor.execute("SELECT MAX(id) FROM train")
        result = mycursor.fetchall()
        train_id = 1
        try:
            for i in result:
                train_id = int(i[0])+1
                break
        except:
            pass
        seats_filled = 0

        while 1:
            class_type = input("\nEnter class : ").strip()
            price = int(input("\nEnter price : "))
            seats = int(input("\nEnter total number of seats : "))
            sql = "INSERT INTO train (id,source,destination,class_type,price,seats) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (train_id, source, destination, class_type, price, seats)
            mycursor.execute(sql, val)
            mydb.commit()
            opt = input("\nDo you want to add another class? y/n :").strip()
            if opt != 'y':
                break
        opt = input("\n\nDo you want to add another train? y/n :").strip()
        if opt != 'y':
            break
