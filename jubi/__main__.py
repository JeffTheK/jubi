import calendar
import colorama
import click
from calendar import monthrange
from datetime import datetime
from colorama import Fore, Back, Style

@click.command()
@click.option('-m', '--month', default=-1)
@click.option('-y', '--year', default=-1)
def main(month, year):
    colorama.init()

    current_time = datetime.today()
    if month != -1:
        current_time.replace(month=month)
    if year != -1:
        current_time = current_time.replace(year=year)
    
    days_count = monthrange(current_time.year, current_time.month)[1]
    print(current_time.strftime("%B %Y").center(21))
    print(f"{Fore.YELLOW}Su Mo Tu We Th Fr Sa{Fore.RESET}")
    days = calendar.monthcalendar(current_time.year, current_time.month)
    for row in days:
        for char in row:
            if row.index(char) == 5 or row.index(char) == 6:
                print(Fore.GREEN, end = "")
            if char == current_time.day:
                print(Fore.CYAN + Style.BRIGHT, end="")
            if char != 0 and char < 10:
                print(" " + str(char) + " ", end="")
            elif char != 0 and char >= 10:
                print(str(char) + " ", end="")
            else:
                print("   ", end="")
            print(Fore.RESET + Style.RESET_ALL, end="")
        print()