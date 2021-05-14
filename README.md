# CSC_322_Project
TEAM Z: Sakib Amin, Nezar Vidad, Mike Neri

An online computer store built using Python and Tkinter GUI library

# Initialize Database

Requirements: 
* Python
* mySQL connnector for Python
* MySQL

Unfortunately, since we did not fully decide on how to connect to the database you will have to edit
your password/root in several locations. The following files you must change the datbase credentials (will change later):

``` python
# change to your credentials

con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "dbvb72^^DATAf2fa1#$",
        database = "computer_store",
        port = 3306
)
```

* db_connector.py
* Connect_DB.py
* User_Login_Functions.py
* Store_Clerk_GUI.py
* Registration_Interface.py
* Registered_GUI.py
* Part_Company_Functions.py
* Login_Interface.py
* Delivery_Company_GUI.py
* Computer_Part_Company_GUI.py
* Buy_GUI.py
* Build_Your_Own_Interface.py

Again, hopefully when you are reading this, the amount of files has been reduced to a single one.

Next please run the new_db.sql file in order to create the databse and fill in entires.

# Run the program

Please do the following steps:

```bash
$ git clone https://github.com/SakibAmin/CSC_322_Project.git
```

```bash
$ cd CSC_322_Project
```

```bash
$ python Start.py
```

# Moving through the app

In the database you will see tables for users, when you run Start.py you will be prompted to login.
Please explore the the privileged accounts using the ones we made since you cannot sign up for a privileged user.

Thanks for reading!
