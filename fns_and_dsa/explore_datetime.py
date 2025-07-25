import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date_and_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_date_and_time)
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.datetime.now()
    future_date = today + timedelta(days)
    print(future_date.strftime("%Y-%m-%d"))