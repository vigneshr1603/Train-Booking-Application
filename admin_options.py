from add_train_details import *
from display_train_details import *
from view_bookings import *
from delete_train import *


def admin_options():
    while 1:
        option = input("\nSelect one option - \n Add a train  - 1 \n Delete a train - 2 \n Available train details - 3 \n View customer bookings - 4 \n Logout - 5\n").strip()
        if option == '1':
            add_train_details()
        elif option == '2':
            delete_train()
        elif option == '3':
            display_train_details()
        elif option == '4':
            view_bookings()
        else:
            print("\nYou are Logged out\n")
            return
