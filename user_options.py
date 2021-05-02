from view_my_bookings import * 
from display_train_details import *
from book_ticket import *
from cancel_train import *



def user_options(user_id):
    while 1:
        option=input("Select an option\n 1-Available Trains\n 2-Book a ticket\n 3-View my bookings\n 4-Cancel ticket\n 5-Logout\n").strip()
        if option=='1':
            display_train_details()
        elif option=='2':
            book_ticket(user_id)
        elif option=='3':
            view_my_bookings(user_id)
        elif option=='4':
            train_id=int(input("\nEnter train id - ").strip())
            seat_no=input("\nEnter class - ").strip()
            cancel_train(user_id,train_id,seat_no)
        else:
            break
        

