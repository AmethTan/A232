import functions
import getpass
import sys
import pandas as pd

admin_ic_number = "020225141129"
admin_password = "1129"
filename = "tax_records.csv"

# Tax Calculation
def tax_calculation():
    income = float(input("Enter your annual income: "))
    if input("Do you want to calculate your tax reliefs? (yes/no) ").upper() == "YES":
        tax_relief = functions.calculate_relief()
        print("Your tax relief total is: RM {:.2f}".format(tax_relief))
    else :
        tax_relief = float(input("Enter your tax relief amount: "))
    tax_payable = functions.calculate_tax(income, tax_relief)
    data = {"IC Number": ic_number, "Income": income, "Tax Relief": tax_relief, "Tax Payable": tax_payable}
    functions.save_to_csv(data, filename)
    print("Your tax payable is: RM {:.2f}".format(tax_payable))
    print("Your tax records have been saved to {}.".format(filename))
    
# Main Body
def main():
    while True:
        print("Functions: ")
        print("1. Tax Calculation")
        print("2. Tax Reliefs")
        print("3. Tax Records")
        print("4. Exit")

        admin_input = int(input("Function to perform: "))
        if admin_input == 1: 
            tax_calculation()
        elif admin_input == 2: 
            tax_relief = functions.calculate_relief()
            print("Your tax relief total is: RM {:.2f}".format(tax_relief))
        elif admin_input == 3: 
            if functions.read_from_csv(filename) is None:
                print("No existing tax records found.")
            else:
                print("Existing tax records found.")
                df = functions.read_from_csv(filename)
                print(df.to_string())
        elif admin_input == 4: 
            sys.exit()
        else:
            print("Invalid input. Please enter (1/2/3/4).")

# User registration prompt 
while True:
    if input("Are you a registered user? (yes/no) ").upper() == "NO":
        ic_number = input("Enter your IC number: ")
        password = getpass.getpass("Enter the last 4 digits of your IC number: ")
        if functions.verify_user(ic_number, password):
            print("Registration successful.")
            print("Please enter your password again to enter the program.")
        break
    elif input("Are you a registered user? (yes/no) ").upper() == "YES":
        ic_number = input("Enter your IC number: ")
        break
    else:
        print("Invalid Input. Please try again.")

password = getpass.getpass("Enter your password: ")
if functions.verify_user(ic_number, password):
    if ic_number == admin_ic_number and password == admin_password:
        main()
    else: 
        print("Welcome To Tax Input Program, {}!".format(ic_number))
        tax_calculation()
        print("Please inquire the admin for previous tax records.")
else:
    print("Invalid IC number or password.")
    sys.exit()      