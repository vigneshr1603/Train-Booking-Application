# Train-Booking-Application

## Clone And Use

- This is a console application which is completely built using `python` and `mySQL`.
- Make sure you have `python` and `MySQL` installed in your system.
- Make sure you install `python-tabulate` library in python. You can use the following command to install. To know more visit [here](https://pypi.org/project/tabulate/).

     - ```python
          pip install tabulate
       ```

## Customize

### mysql_connector.py

The file looks like below:

```python 
import mysql.connector;



mydb = mysql.connector.connect(
    host="localhost",
    user="root",     # <-- change the username here
    password="password",   # <---- change the password here
    database="train_booking_application"

)

```
Enter the username and password of your MySQL in the respective fields.

### initializer.py

The file looks something like below:

```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # <-- change the username here
    password="password",    # <---- change the password here
)
mycursor = mydb.cursor()
```
Enter the username and password of your MySQL in the respective fields.

## Running the Appliation

### initializer.py

You will find a file named  `initializer.py`.  After making the above changes run this file.  A database named  `train_booking_application`  will be created in your MySQL.


### login.py

You will find a file named  `login.py`.  After executing  `initializer.py`  run this file.  Happy Coding 👍.

