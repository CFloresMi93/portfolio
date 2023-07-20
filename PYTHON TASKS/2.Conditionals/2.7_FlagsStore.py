'''Program will calculate the price of a flag depending on its size in 
square centimeters, an embroidered shield and if shipping costs are paid.

Each square centimeters costs 0.02€
Embroidered shield costs 2.5€
Shipping costs 5€

'''

def additionalCosts (element, increment):
    global price
    if element == 'y':
        price = price + increment


height = float(input('What is the flag height in square centimeters?\n'))
width = float(input('What is the flag width in square centimeters?\n'))

price = height * width * 0.02

shield = input('Do you want an embroidered shield (+2.5€)?\n(y/n)\n')
shipping = input('Do you want your flag sent to you (+5€)?\n(y/n)\n')

additionalCosts (shield, 2.5)
additionalCosts (shipping, 5)

print('Your flag will cost ' + str(price) + '€.')