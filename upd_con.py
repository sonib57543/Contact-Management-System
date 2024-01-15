# Update Contact Details.

import mysql.connector as msc

def update_contact():
    try:
        # Establish a connection
        con = msc.connect(host = "localhost", user = "root", passwd = "Sonib#1012", database = "contact")

        # creating cursor Obj.
        cur = con.cursor()

         #design the query
        print("\nData Updated Based on mobile no:-")

        old_mobno = input("\tEnter Mobile No: ")
        if old_mobno.isdigit() and len(old_mobno) == 10:

            print("\nEnter Letest Updated Details:-")

            new_mobno = input("\tEnter Updated Mobile No.: ")
            if new_mobno.isdigit() and len(old_mobno) == 10:

                name = input("\tEnter Updated Name: ")
                if all(w.isalpha() for w in name.split()):

                    add = input("\tEnter Updated Address: ")
                    email = input("\tEnter Updated Email-ID: ")
                    cur.execute("UPDATE contact_book SET mobile_no = '%s', name = '%s', address = '%s', email = '%s' WHERE mobile_no = '%s'" %((new_mobno, name, add, email, old_mobno)))
                    con.commit()
                    print("="*50)
                    
                    if cur.rowcount > 0:
                        print("{} Contact Record Updated... ".format(cur.rowcount))
                    else:
                        print("Contact Record Does Not Exist.")
                else:
                    print("Name should not contain numbers or any special symbols")
                    print("="*50)
            else:
                print("\tPlease Enter Proper 10 Digit of Your Number.--Enter Again ")
        else:
            print("\tPlease Enter Proper 10 Digit of Your Number.--Enter Again ")
    
    except msc.DatabaseError as dbe:
        print("Problem In DataBase: ", dbe)

