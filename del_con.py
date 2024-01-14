# Delete Contact

import mysql.connector as msc
import sys

def delete_contact():
    while True:
        try:
            # Establish a connection
            con = msc.connect(host = "localhost", user = "root", passwd = "Sonib#1012", database = "contact")

            # Create cursor Obj.
            cur = con.cursor()

            name = input("\nEnter Name:")
            if all(w.isalpha() for w in name.split()):

                # Execute MySQL querie 
                cur.execute("DELETE FROM contact_book WHERE name = '%s'" %name)
                con.commit()
                print("-"*50)
                print("{} Contact Deleted Successfully...\n".format(cur.rowcount))
            else:
                print("\tName should not contain numbers or any special symbols.")
            
            while True:
                ch = input("Do you want to delete any other contact? (Y/N): ")
                if ch.upper() == 'Y':
                    break
                elif ch.lower() == 'n':
                    sys.exit()
                else:
                    print("\tInvalid option. Please enter 'Y' or 'N'.\n") 


        except msc.DatabaseError as dbe:
            print("Problem in Database: ", dbe)

