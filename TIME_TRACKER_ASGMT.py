
#importing python libraries needed
from datetime import datetime 
from datetime import timedelta
import csv

# Printing a message out to the user to understand what to do
print('\nTime Tracker')
print('Please Enter Date and Time at start of work')
print('-------------------------------------------')

# notify user to enter date and time in the required format
start_date = input('Enter start of work date in format - DD-MM-YYYY : ')
start_time = input('Enter start of work time in format - H:M AM/PM : ')
print('\n')
print('--------------------------------------------------------------------')
stop_date = input('Enter end of work date in format - DD-MM-YYYY :')
stop_time = input('Enter end of work time in format - H:M AM/PM :')

# using the datetime module, converted the string entered into datetime object
start_datetime_str = f'{start_date} {start_time}'
start_datetime_obj = datetime.strptime(start_datetime_str, '%d-%m-%Y %H:%M %p')

stop_datetime_str = f'{stop_date} {stop_time}'
stop_datetime_obj = datetime.strptime(stop_datetime_str, '%d-%m-%Y %H:%M %p')


# a function to check if the time is AM or PM in the 12 Hour format and return usable start date and time
def datetime_returner(datetime_object, datetime_string):
    if datetime_object.hour < 12:
        if datetime_string[-2:].upper() == 'PM':
            start_date = datetime_object + timedelta(hours=12)
            return start_date
        elif datetime_string[-2:].upper() == 'AM':
            start_date = datetime_object
            return start_date
    else:
        if datetime_string[-2:].upper() == 'AM':
            start_date = datetime_object - timedelta(hours=12)
            return start_date
        elif datetime_string[-2:].upper() == 'PM':
            start_date = datetime_object
            return start_date


# deriving the useful datetime needed for computation
start_datetime = datetime_returner(start_datetime_obj, start_datetime_str)
stop_datetime = datetime_returner(stop_datetime_obj, stop_datetime_str)

# getting the time differeence between the start time and stop time
time_difference = stop_datetime - start_datetime

# splitting the time_difference on the : and get the first index as hour and convert the string to integer
hours = int(str(time_difference).split(':')[0])

# splitting the time_difference on the : and get the second index as minute and covert the string to integer
minutes = int(str(time_difference).split(':')[1])

# convertting the minutes to a decimal value
decimal_minute = (minutes * 0.5) / 30

# obtaining the actual time worked by adding the hour to decimal_minute
time_worked = hours + decimal_minute

# calculate the money made by multiplying as below
amount_made = round((time_worked * 5), 2)

# print the results to the user as below
print(f'Hello, you worked for {hours} hours, {minutes} minutes and made $ {amount_made}')
