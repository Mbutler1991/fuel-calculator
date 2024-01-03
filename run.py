'''
Fuel Price Calculator

This calculates journey cost using current fuel price,
distance travelled and MPG of vehicle used.
'''

import os
import gspread
from google.oauth2.service_account import Credentials
from termcolor import colored
from tabulate import tabulate
import pyfiglet

# Scope for Google Sheets
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Credentials/integrating with Google Sheets
script_dir = os.path.dirname(os.path.realpath(__file__))
creds_path = os.path.join(script_dir, 'creds.json')
CREDS = Credentials.from_service_account_file(creds_path)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fuel_calculator')
data = SHEET.worksheet('data')
COL_INDEX = 1
values_column = data.col_values(COL_INDEX)
result = data.get_all_values()


def get_last_used_row(sheet, column):
    '''
    Function to get the last used row in a column
    '''
    values = sheet.col_values(column)
    last_used_row = len(values) + 1 if values else 1
    return last_used_row


def get_float_input(prompt, min_value, max_value):
    '''
    Function to ensure all data is in valid and no blank inputs
    '''
    while True:
        try:
            user_input = float(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                raise ValueError(f"Invalid input. Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def fuel_price():
    '''
    Function to get the current fuel price as user input
    '''
    print(colored('Please enter current fuel price in cents', 'blue'))
    print(colored('For example 1 euro = 100', 'blue'))
    fp_input = get_float_input('Enter fuel price here:\n', 100.0, 290.0)
    row = get_last_used_row(data, 1)
    data.update_cell(row, 1, fp_input)
    print(colored('Thank you!', 'green'))
    return fp_input


def travel_distance():
    '''
    Function to get the distance traveled as user input
    '''
    print(colored('Please enter the distance traveled in kilometers', 'blue'))
    dist = get_float_input('Enter distance here:\n', 1, 2000)
    row = get_last_used_row(data, 2)
    data.update_cell(row, 2, dist)
    print(colored('Thank you!', 'green'))
    return dist


def miles_per_gallon():
    '''
    Function to get the current MPG of the vehicle as user input
    '''
    print(colored('Please enter current MPG of your vehicle', 'blue'))
    mpg = get_float_input('Enter MPG here:\n', 1, 565)
    row = get_last_used_row(data, 3)
    data.update_cell(row, 3, mpg)
    print(colored('Thank you!', 'green'))
    return mpg


def calculate_cost(mpg, td, fp):
    '''
    Function to calculate the cost of the journey
    '''
    kml = float(mpg) / 2.3521458
    litres_used = td / kml
    cost_cents = litres_used * fp
    cost_euro = cost_cents / 100
    rounded_cost_euro = round(cost_euro, 2)
    print(colored('The estimated cost of your journey is:', 'blue'), colored(rounded_cost_euro, 'green', attrs=['reverse']))
    row = get_last_used_row(data, 4)
    data.update_cell(row, 4, rounded_cost_euro)


def display_results():
    """
    Function to display summary of results for this journey
    """
    headers = ["Fuel Price", "Travel Distance", "MPG", "Estimated Cost"]
    data_values = data.get_all_values()

    journey = [next((value for value in reversed(col) if value.strip()), "") for col in zip(*data_values)]

    table_data = [headers] + [journey]
    table = tabulate(table_data, tablefmt="fancy_grid")

    print(colored('Your Journey:', 'green', 'on_white', attrs=['underline']))
    print(table)


def main():
    '''
    main function to run the program
    '''
    fp = fuel_price()
    td = travel_distance()
    mpg = miles_per_gallon()
    calculate_cost(mpg, td, fp)
    display_results()

title = pyfiglet.figlet_format("Fuel Cost Calculator")
print(title)
print(colored('Welcome to the fuel price calculator', 'red', attrs=['reverse']))
main()

while True:
    try:
        print(colored('Would you like to start over (y/n)?', 'cyan'))
        repeat = input('y/n?')
        if repeat.upper() == 'Y':
            main()
        elif repeat.upper() == 'N':
            print(colored('Thank you for choosing our fuel price calculator', 'red', 'on_white'))
            exit()
        else:
            raise ValueError("Invalid input. Please enter a y or n.")
    except ValueError:
        print('Invalid input. Please enter y or n')
