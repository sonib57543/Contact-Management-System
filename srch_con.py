# Search Contact

import sys
import mysql.connector as msc

def search_contact():
    while True:
        print("Select The Search Criteria:")
        print("\t1.Mobile_No.")
        print("\t2.Name")
        print("\t3.Address")
        print("\t4.Email")
        print("\t5.Cancle")
        
        try:
            # Establish a connection
            con = msc.connect(host = "localhost", user="root", passwd="Sonib#1012", database="contact")

            # creating cursor Obj.
            cur = con.cursor()

            ch = int(input("Enter Your Choice: "))

            if ch == 1:
                print("=>Searching by Mobile Number")
                print("="*50)
                try:
                    mno = int(input("Enter Mobile No:"))
                    if len(str(mno)) == 10:
                        print("-"*50)
                    
                        # Execute MySQL querie
                        cur.execute("SELECT*FROM contact_book WHERE mobile_no ='%s'" %mno)
                        records = cur.fetchall()
                        if len(records) > 0:
                            for rec in records:
                                print("Mobile No = ", rec[0])
                                print("Name = ", rec[1])
                                print("Address = ",rec[2])
                                print("Email-Id = ", rec[3])
                                print("="*50)
                        else:
                            print("'{}' related contact Record does not Exist\n".format(mno))
                    else:
                        print("Please Enter Proper 10 Digit of Your Number. ")
                except ValueError:
                    print("The mobile number should be numeric.")
            elif ch == 2:
                print("=>Searching by Name")
                print("="*50)
                name = input("Enter Name:")
                if all(w.isalpha() for w in name.split()):
                    # Execute MySql Querie
                    cur.execute("SELECT*FROM contact_book WHERE name ='%s'" %name)
                    records = cur.fetchall()
                    if len(records) > 0:
                        for rec in records:
                            print("Mobile No = ", rec[0])
                            print("Name = ", rec[1])
                            print("Address = ",rec[2])
                            print("Email-Id = ", rec[3])
                            print("="*50)
                    else:
                        print("'{}' related contact Record does not Exist\n".format(name))
                else:
                    print("\tName should not contain numbers or any special symbols")
                    print("="*50)

            elif ch == 3:
                print("=>Searching by Address")
                print("="*50)
                add = input("Enter Address:")
                print("-"*50)

                # Execute MySql Querie
                cur.execute("SELECT*FROM contact_book WHERE address ='%s'" %add)
                records = cur.fetchall()
                if cur.rowcount > 0:
                    for rec in records:
                        print("Mobile No = ", rec[0])
                        print("Name = ", rec[1])
                        print("Address = ",rec[2])
                        print("Email-Id = ", rec[3])
                        print("="*50)
                else:
                    print("'{}' related contact Record does not Exist\n".format(add))
            elif ch == 4:
                print("=>Searching by Email")
                print("="*50)
                mail = input("Enter Email-ID:")
                print("-"*50)

                # Execute Mysql Querie
                cur.execute("SELECT*FROM contact_book WHERE email ='%s'" %mail)
                records = cur.fetchall()
                if cur.rowcount > 0:
                    for rec in records:
                        print("Mobile No = ", rec[0])
                        print("Name = ", rec[1])
                        print("Address = ",rec[2])
                        print("Email-Id = ", rec[3])
                        print("="*50)
                else:
                    print("'{}' related contact Record does not Exist\n".format(mail))
            elif ch == 5:
                print("Exiting the program. Thank you!")
                sys.exit()
            else:
                print("\tInvalid choice. Please try again.\n")
        except ValueError:
            print("Plese Enter Valid Option.")
        except msc.DatabaseError as dbe:
            print("Problem In Database: ", dbe)
        finally:
        # Close the cursor and connection
            if con.is_connected():
                cur.close()
                con.close()

        while True:
            op = input("\tDo You Want To Search Another Contact No. (Y/N): ")
            if op.upper() == 'N':
                print("\tThank You..")
                sys.exit()
            elif op.lower() == 'y':
                break
            else:
                print("Invalid option. Please enter 'Y' or 'N'.")
