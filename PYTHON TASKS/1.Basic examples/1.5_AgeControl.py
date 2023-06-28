age = int(input('How old are you?'))

if age < 18:
    print('You will be adult in ' + str(18 - age))
else:
    print('You are already an adult')