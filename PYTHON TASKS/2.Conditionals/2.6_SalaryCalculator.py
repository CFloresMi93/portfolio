''' Program will calculate your salary if you give it the number of hours 
you worked. You earn 10€/per hour the first 40 hours and 12€/per each 
extra hour.'''

hours = int(input('¿How many hours did you work this week?'))

if hours <= 40:
    salary = hours * 10
else:
    extraHours = hours - 40
    salary = (40 * 10) + (extraHours * 12)

print('Your salary this week is ' + str(salary) + '€.')