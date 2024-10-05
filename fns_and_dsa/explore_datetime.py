#!/usr/bin/env python3
from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now().date()
    future_date = current_date + timedelta(days=days)
    print("Future Date:", future_date)
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
