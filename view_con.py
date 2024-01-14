# View Contact

import mysql.connector as msc

def view_contacts():
    try:
        # Establish a connection
        con = msc.connect(host="127.0.0.1", user="root", passwd="Sonib#1012", database="contact")

        # Creating cursor object
        cur = con.cursor()

        # Execute MySQL query 
        cur.execute("SELECT * FROM contact_book ORDER BY NAME")
        records = cur.fetchall()

        # Displaying results with numbering
        for i, record in enumerate(records, start=1):
            print("-" * 50)
            print("{}. Contact Detail:".format(i))
            print("\tMobile No: ", record[0])
            print("\tName: ", record[1])
            print("\tAddress: ", record[2])
            print("\tEmail-Id: ", record[3])

    except msc.DatabaseError as dbe:
        print("Problem in MySQL Database: ", dbe)

    finally:
        # Close the cursor and connection
        if con.is_connected():
            cur.close()
            con.close()

