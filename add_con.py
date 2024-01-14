# Add New Contact.

import mysql.connector as msc
import sys

def add_new_contact():
    try:
        # Establish a connection
        con = msc.connect(host = "localhost",user = "root", passwd = "Sonib#1012", database = "contact")

        # Creating cursor Obj.
        cur = con.cursor()

        mobile_no = input("Enter Mobile No: +91-")
        if mobile_no.isdigit() and len(mobile_no) == 10:

            name = input("Enter Name: ")
            if all(w.isalpha() for w in name.split()):
                address = input("Enter Address: ")
                email = input("Enter Email-ID: ")

                # Execute MySQL querie 
                cur.execute("INSERT INTO contact_book Values('%s', '%s', '%s', '%s')" %(mobile_no, name, address, email))
                con.commit()

                print("-"*50)
                print("{} Contact Saved Successfully...\n".format(cur.rowcount))
            else:
                print("\tName should not contain numbers or any special symbols.")
                print("="*50)
            
        else:
            print("\tPlease Enter Proper 10 Digit of Your Number.--Enter Again ")
    except msc.DatabaseError as dbe:
        print("Problem in MySql Database: ",dbe)

    finally:
        # Close the cursor and connection
        if con.is_connected():
            cur.close()
            con.close()

