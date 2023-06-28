'''Program that asks you how many slices of cake there are, 
how many people will be eating cake, and returns how many slices 
of cake each person gets and how many slices of cake are left over.
'''

slices = int(input('How many slices of cake there are?'))
people = int(input('How many people are going to eat cake?'))

slicesPerPerson = round(slices / people)
slicesRemain = slices % people

print('Each person can eat ' + str(slicesPerPerson) + ' slices of cake and will remain ' + str(slicesRemain))
