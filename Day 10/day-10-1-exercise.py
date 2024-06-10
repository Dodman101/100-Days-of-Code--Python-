def is_leap(year):
    """ Takes the year as input and checks if it is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """ Takes the year and month as inputs and checks if the year is a leap year and returns 29 days for February else returns the number of days in a particular month."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

#Do not Change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)