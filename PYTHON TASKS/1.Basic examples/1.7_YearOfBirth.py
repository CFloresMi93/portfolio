from datetime import date

age = int(input('How old are you?'))

year = date.today().year

print('Your birth year is ' + str(year - age))
