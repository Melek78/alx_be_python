import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date_and_time = current_date.strftime("YYYY-MM-DD HH:MM:SS")
    print(formatted_date_and_time)
def calculate_future_date():
    days = int(input("Enter number of days: "))
    today = datetime.datetime.now()
    future_date = today + timedelta(days)
    print(future_date.strftime("YYYY-MM-DD"))