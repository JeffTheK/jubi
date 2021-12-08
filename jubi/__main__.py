import calendar
from calendar import monthrange
from datetime import datetime

def main():
    current_time = datetime.today()
    days_count = monthrange(current_time.year, current_time.month)[1]
    print("Su Mo Tu We Th Fr Sa")
    days = calendar.monthcalendar(current_time.year, current_time.month)
    for row in days:
        for char in row:
            if char != 0 and char < 10:
                print(" " + str(char) + " ", end="")
            elif char != 0 and char >= 10:
                print(str(char) + " ", end="")
            else:
                print("   ", end="")
        print()