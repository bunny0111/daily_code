'''
(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
Write a python program to check if a year is a leap year.
'''
def LeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "It is leap year."
    return "It is not a leap year."

print(LeapYear(2012))
print(LeapYear(2017))