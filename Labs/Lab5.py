from datetime import datetime

def calculate_seconds_old(birthdate):
    current_datetime = datetime.now()

    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
  
    seconds_old = (current_datetime - birthdate).total_seconds()

    return seconds_old

birthdate = input("Enter your birthday (YYYY-MM-DD): ")

try:
    seconds_old = calculate_seconds_old(birthdate)
    print("You are approximately", seconds_old, "seconds old.")
except ValueError:
    print("Invalid date format. Please enter the date in the format 'YYYY-MM-DD'.")
