import sys
from add_con import add_new_contact
from view_con import view_contacts
from srch_con import search_contact
from upd_con import update_contact
from del_con import delete_contact

def main():
    print("="*50)
    print("  Welcome To Contact Management System")
    while True:
        print("="*50)
        print("\t1.Add New Contact")
        print("\t2.View Contact")
        print("\t3.Search Contact")
        print("\t4.Update Contact")
        print("\t5.Delete Contact")
        print("\t6.Exit")
        
        try:
            ch = int(input("Enter Your Choice: "))  
            match ch:
                case 1:
                    print("\n\t\tNew Contact")
                    print("*"*50)
                    add_new_contact()
                case 2:
                    print("\n=> The Contact details are as follows:")
                    view_contacts()
                case 3:
                    print("\n\t=>Search Contact")
                    print("-"*50)
                    search_contact()
                case 4:
                    print("\n\t=>Update Contact")
                    print("-"*50)
                    update_contact()
                case 5:
                    print("\n\t=>Delete Contact")
                    print("-"*50)
                    delete_contact()

                case 6:
                    print("Thank You!")
                    sys.exit()
                case _:
                    print("\tWrong Choice---try again")
        except ValueError:
            print("Plese Enter Valid Option.")

        while True:
            print("="*50)
            op = input("\n\tWant To Contine (Y/N): ")
            if op.upper() == 'N':
                print("\tThank You..")
                sys.exit()
            elif op.lower() == 'y':
                break
            else:
                print("Invalid option. Please enter 'Y' or 'N'.\n")



# Main Program
main()
