# Fuel Cost Calculator

This project was ade using Python, Google Sheets, Google Cloud Services and Google Drive api. and it is sued to get an estimate of how much petrol or diesel you need for a journey

This application is aimed at anybody that drives a car as it can be used with MPG for any vehicle it can get an estimate of price for any vehicle and any journey.

The aim is to help people manage their finances better when it comes to their travel costs and to help them with their budget.

I would ideally like to introduce this to motorists by word of mouth and a targetted ad campaign.

## User Stories

- As a road user, I can check costs for unusually long journeys, so I can be prepared before I set off so I don't run out of fuel.
- As a parent, I can plan journeys in advance, so I don't overspend on petrol and can keep money in the family budget.
- As a teacher, I can use the maths on this app, so I can help teach kids about mile to kilometre conversions and MPG to K/L conversions.
- As a frequent road user, I can use the database, to keep track of my journeys and changes in cost.

## Flowchart

Flowchart was created with Canva and some changes have been made since this stage.

![Wireframe](https://github.com/Mbutler1991/Koh-iNoor/blob/master/assets/Screenshots/wireframe.png) 

## Data Storage

The data for the application ie fuel price, travel distance, MPG and journey cost is stored in a google sheet. You can view the sheet [here](https://docs.google.com/spreadsheets/d/1pIAS9SkPGWzBjLZG3S6vO8TamaAEemttbZBdWit8Eck/edit?pli=1#gid=1680754323).

## Features 

- __First__

- This is the first screen that shows up
- It features a title, a welcome message and the first question

- __Title__

- This is the first screen that shows up
- The title is designed using pyfiglet

- __Fuel Price__

- This is the first question
- It asks for your fuel price in cents and has an area for user input
- Information entered here is stored in worksheet in google sheets
- Colours are made using termcolor

- __Travel Distance__

- This is the first question
- It asks for your travel distance in kilometres and has an area for user input
- Information entered here is stored in worksheet in google sheets
- Colours are made using termcolor

- __MPG__

- This is the third and final question
- It asks for the average MPG of your vehicle and has an area for user input
- Information entered here is stored in worksheet in google sheets
- Colours are made using termcolor

- __Results__

- This is the results section
- It shows you based off your input the estimated cost for the journey
- It also shows a table using tabulate with the data you inputted and the cost of the journey
- Information here is stored in worksheet in google sheets
- Colours are made using termcolor

-__Worksheet__

- This is the worksheet where the data is stored
- The user input data is stored in the first three columns
- The result of the program is stored in the fourth column
- This is connected using Google Cloud service and the Google Drive API and Google Sheets API
- Installed Gspread and Google-Auth python libraries to make this possible

## Future Implementations

I would like to add in features for travelling between countries, this way I could factor it to work based off different currencies, price formats, and measurements ie miles instead of kilometers and that the program would handle all the conversions so you could always see a result in your home currency. I also would like to allow for multinational trips so you would be able to work out multiple different measurements to work out a journey that uses multiple different currencies and multiple different prices at multiple different filling stations and return a more accurate estimate of total journey cost. I would also like to add in features to recall data from the worksheet to work out average costs of fuel and journeys.

## Technology

- This program was coded with Python
- HTML, CSS and JavaScript were used in Code Institute Template
- Pyfiglet Library was used to add style to the title
- Termcolor was used to add colours to print statements in the terminal for added user experience
- Gspread and Google-Auth were used to integrate the fuel_calculator worksheet to store and access user inputs and results
- Canva was used to create was used to create flowchart at design stage
- Git was used for version control
- Github was used to store repository
- Heroku was used to deploy the project
- VS Code was used for all code

## Testing 

-__Manual Testing__

- Fuel Price input
  - Checked this field with multiple different invalid entries including blank space, string, out of range value, bool. Error raised every time and advised user of invalid input and requests input again.

- Travel Distance input
  - Checked this field with multiple different invalid entries including blank space, string, out of range value, bool. Error raised every time and advised user of invalid input and requests input again.

- MPG input
  - Checked this field with multiple different invalid entries including blank space, string, out of range value, bool. Error raised every time and advised user of invalid input and requests input again.

- Restart input
  - Checked this field with multiple different invalid entries including blank space, string, out of range value, bool. Error raised every time and advised user of invalid input and requests input again.

- Worksheet
  - Checked this field with multiple different invalid entries including blank space, string, out of range value, bool. Error raised every time and advised user of invalid input and requests input again.
