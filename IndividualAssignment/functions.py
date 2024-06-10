import pandas as pd
import taxReliefDescription as tRD
import os

''' Verify the user's credentials by checking if the IC number is 
12 digits long and if the password matches the last 4 digits of the IC '''
def verify_user(ic_number, password) :
    return len(ic_number) == 12 and password == ic_number[-4:]

'''Calculate the tax relief obtainable based on the Malaysian tax reliefs
 for the current year'''
def calculate_relief() :
    print("Below are the tax reliefs offered by the Malaysian government to individual:")
    tRD.tax_relief_description()
    print("According to the descriptions. Please enter the amount for each type of reliefs from 1 to 21.")
    tax_relief = 0
    tax_relief += float(input("1. "))
    tax_relief += float(input("2. "))
    tax_relief += float(input("3. "))
    tax_relief += float(input("4. "))
    tax_relief += float(input("5. "))
    tax_relief += float(input("6. "))
    tax_relief += float(input("7. "))
    tax_relief += float(input("8. "))
    tax_relief += float(input("9. "))
    tax_relief += float(input("10. "))
    tax_relief += float(input("11. "))
    tax_relief += float(input("12. "))
    tax_relief += float(input("13. "))
    tax_relief += float(input("14. "))
    tax_relief += float(input("15. "))
    tax_relief += float(input("16a. "))
    tax_relief += float(input("16b. "))
    tax_relief += float(input("16c. "))
    tax_relief += float(input("17. "))
    tax_relief += float(input("18. "))
    tax_relief += float(input("19. "))
    tax_relief += float(input("20. "))
    tax_relief += float(input("21. "))
    return tax_relief

'''Calculate the tax payable based on the Malaysian tax rates for the 
current year'''
def calculate_tax(income, tax_relief) :
    if tax_relief > income: 
        tax_relief = income
    chargeable_income = income - tax_relief
    tax_rate = {
        # Chargeable Income Category
        "CIC":[
            0,5000,20000,35000,50000,70000,100000,400000,600000,2000000
        ],
        "Base Tax":[0,0,150,600,1500,3700,9400,84400,136400,528400],
        "Rate":[0,1,3,6,11,19,25,26,28,30]
    }
    tax_table = pd.DataFrame(tax_rate)

    # tax_table reverse rows 
    ttrr = tax_table.iloc[::-1]

    for ind in ttrr.index:
        if chargeable_income >= ttrr["CIC"][ind]:
            tax = ((chargeable_income - ttrr["CIC"][ind]) * ttrr["Rate"][ind] / 100) + ttrr["Base Tax"][ind]
            break
    
    return tax

'''Save the user's data (IC number, income, tax relief, and tax payable) 
to a CSV file. If the file doesn't exist, create a new file with a header
 row. If the file exists, append the new data to the existing file '''
def save_to_csv(data, filename):
    header = ["IC Number", "Income", "Tax Relief", "Tax Payable"]
    if not os.path.exists(filename):
        # Create a new file with the header
        df = pd.DataFrame(columns=header)
        df.to_csv(filename, index=False)
    # Append the new data to the existing file
    df = pd.DataFrame([data], columns=header)
    df.to_csv(filename, mode='a', header=False, index=False)

'''Read data from the CSV file and return a pandas DataFrame containing 
the data. If the file doesn't exist, return None.'''
def read_from_csv(filename) :
    try:
        return pd.read_csv(filename, dtype=str, keep_default_na=False)
    except FileNotFoundError:
        return None