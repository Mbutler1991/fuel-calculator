import gspread
import os
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
    values = sheet.col_values(column)
    last_used_row = len(values) + 1 if values else 1
    return last_used_row

def fuel_price():
    print('Please enter current fuel price')
    fuel_price_input = input('Enter fuel price here:\n')

    if 100.0 <= float(fuel_price_input) <= 290.0:
        row = get_last_used_row(data, 1)
        data.update_cell(row, 1, fuel_price_input)
        print('Thank you!')
        return float(fuel_price_input)
    else:
        raise ValueError("Invalid fuel price")

def travel_distance():
    print('Please enter the distance traveled in kilometers')
    dist = input('Enter distance here:\n')

    if 1 <= float(dist) <= 565:
        row = get_last_used_row(data, 2)
        data.update_cell(row, 2, dist)
        print(colored('Thank you!', 'red', attrs=['reverse', 'blink']))
        return float(dist)
    else:
        raise ValueError("Invalid distance")

def miles_per_gallon():
    print('Please enter current MPG of your vehicle')
    mpg = input('Enter MPG here:\n')

    if 1 <= float(mpg) <= 565:
        row = get_last_used_row(data, 3)
        data.update_cell(row, 3, mpg)
        print('Thank you!')
        return float(mpg)
    else:
        raise ValueError("Invalid MPG")
    
def calculate_cost(mpg, td, fp):
    kml = float(mpg) / 2.3521458
    litres_used = td / kml
    cost_cents = litres_used * fp
    cost_euro = cost_cents / 100
    rounded_cost_euro = round(cost_euro, 2)
    print(rounded_cost_euro)
    row = get_last_used_row(data, 4)
    data.update_cell(row, 4, rounded_cost_euro)

def main():
    try:
        fp = fuel_price()
        td = travel_distance()
        mpg = miles_per_gallon()
        calculate_cost(mpg, td, fp)
    except ValueError as e:
        print(f"Error: {e}")

print('Welcome to the fuel price calculator')
main()
print('Thank you for choosing our fuel price calculator')

print('Welcome to the fuel price calculator')
main()
print('Thank you for choosing our fuel price calculator')