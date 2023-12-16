import os
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


script_dir = os.path.dirname(os.path.realpath(__file__))
creds_path = os.path.join(script_dir, 'creds.json')
CREDS = Credentials.from_service_account_file(creds_path)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fuel_calculator')

data = SHEET.worksheet('data')
col_index = 1
values_column =  data.col_values(col_index)

result = data.get_all_values()

def get_last_used_row(sheet, column):
    '''
    Function to get the last used row in a column
    '''
    values = sheet.col_values(column)
    last_used_row = len(values) + 1 if values else 1
    return last_used_row

def fuel_price():
    '''
    Function to get the current fuel price as user input
    '''
    print(colored('Please enter current fuel price', 'blue'))
    fuel_price_input = input('Enter fuel price here:\n')

    if 100.0 <= float(fuel_price_input) <= 290.0:
        row = get_last_used_row(data, 1)
        data.update_cell(row, 1, fuel_price_input)
        print(colored('Thank you!', 'green'))
        return float(fuel_price_input)
    else:
        raise ValueError("Invalid fuel price")

def travel_distance():
    '''
    Function to get the distance traveled as user input
    '''
    print(colored('Please enter the distance traveled in kilometers', 'blue'))
    dist = input('Enter distance here:\n')

    if 1 <= float(dist) <= 565:
        row = get_last_used_row(data, 2)
        data.update_cell(row, 2, dist)
        print(colored('Thank you!', 'green'))
        return float(dist)
    else:
        raise ValueError("Invalid distance")

def miles_per_gallon():
    '''
    Function to get the current MPG of the vehicle as user input
    '''
    print(colored('Please enter current MPG of your vehicle', 'blue'))
    mpg = input('Enter MPG here:\n')

    if 1 <= float(mpg) <= 565:
        row = get_last_used_row(data, 3)
        data.update_cell(row, 3, mpg)
        print(colored('Thank you!', 'green'))
        return float(mpg)
    else:
        raise ValueError("Invalid MPG")

def calculate_cost(mpg, td, fp):
    '''
    Function to calculate the cost of the trip
    '''
    kml = float(mpg) / 2.3521458
    litres_used = td / kml
    cost_cents = litres_used * fp
    cost_euro = cost_cents / 100
    rounded_cost_euro = round(cost_euro, 2)
    print(colored(rounded_cost_euro, 'green', attrs=['reverse', 'bold']))
    row = get_last_used_row(data, 4)
    data.update_cell(row, 4, rounded_cost_euro)

def main():
    '''
    main function to run the program
    '''
    try:
        fp = fuel_price()
        td = travel_distance()
        mpg = miles_per_gallon()
        calculate_cost(mpg, td, fp)
    except ValueError as e:
        print(colored(f"Error: {e}", 'red', attrs=['bold']))

print(colored('Welcome to the fuel price calculator', 'red', attrs=['reverse']))
main()
print(colored('Thank you for choosing our fuel price calculator', 'red', attrs=['reverse']))

print(colored('Welcome to the fuel price calculator', 'red', attrs=['reverse']))
main()
print(colored('Thank you for choosing our fuel price calculator', 'red', attrs=['reverse']))