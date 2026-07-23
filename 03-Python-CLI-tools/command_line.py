import numpy as np
import pandas as pd

#2. Preview Data
def perview():
    print(f"Total number (Row, Column): {df.shape}\n")
    print(f"Column Name: {df.columns}\n")
    print(df.head(5))

#3. Analyze Numeric Columns
def analyze_column():
    numeric_column = df.select_dtypes(include="number").columns
    print(numeric_column)
    column_3 = input("Enter column name: ")
    for i in numeric_column:
        if column_3 == i:
            while True:
                print("\n----Sub-Menu----")
                print("1. Total")
                print("3. Minimum Value")
                print("4. Maximum Value")
                print("2. Average")
                print("5. Count of Values")
                print("6. Go Back to Main Menu\n")

                option = int(input("Choose your choise: "))
            
                if option == 1:
                    print(f"Add of {column_3}: {df[column_3 ].sum()}")
                elif option == 2:  
                    print(f"Average of {column_3}: {df[column_3 ].mean()}")
                elif option ==3:
                    print(f"Minimum of {column_3}: {df[column_3 ].min()}")
                elif option == 4:
                    print(f"Maximum of {column_3}: {df[column_3 ].max()}")  
                elif option == 5:
                    print(f"Count of {column_3}: {df[column_3 ].count()}") 
                elif option == 6:
                    break  
                else:
                    print("Choose between 1 to 6")


#4. Check Missing Values
def check_missing_value():
    sub_df = df.columns
    column = input("Enter column name: ")
    for i in sub_df:
        if column == i:
            print(f"Missing values in '{column}' are '{df[column].isnull().sum()}'\n")   


#1. Load CSV File

filename = input("Enter file path: ")
try:
    df = pd.read_excel(filename)
    print("File loaded successfully!\n")
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ','_')
    # print(df.column)


    while True:
        print("----Main Menu----")
        print("1. Preview Data")
        print("2. Analyze Numeric Column")
        print("3. Check Missing Values")
        print("4. Exit\n")

        option = int(input("Choose your choise: "))

        if option == 1:
            perview()
        elif option == 2:  
            analyze_column()
        elif option ==3:
            check_missing_value()
        elif option == 4:
            break   
        else:
            print("Choose between 1 to 4")

except FileNotFoundError:
    print("File not found.")



