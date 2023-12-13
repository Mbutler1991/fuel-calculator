import gspread
import os
from google.oauth2.service_account import Credentials

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

result = data.get_all_values()
