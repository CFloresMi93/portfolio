from datetime import date

dateInput = input('Enter time in this format yyyy-mm-dd, the program will say you the weekday.\n').split('-')

year, month, day = [int(item) for item in dateInput]

userDate = date(year, month, day)

weekday = userDate.weekday()

match weekday:
    case 0:
        print('Monday')
    case 1:
        print('Tuesday')
    case 2:
        print('Wednesday')
    case 3:
        print('Thursday')
    case 4:
        print('Friday')
    case 5:
        print('Saturday')
    case 6:
        print('Sunday')
