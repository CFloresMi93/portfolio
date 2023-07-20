# A test exam made with code. Max points 30

points = 0

print('Answer just with the correct letter')

answer = input('What is the chemical formula of Carbon?\na) Ca\nb) C\nc) Cb\n')

if answer == 'b':
    points += 10
else:
    points -= 5

answer = input('What is the result of 1/0 with rational numbers?\na) 1\nb) 0\nc) It is not possible\n')

if answer == 'c':
    points += 10
else:
    points -= 5

answer = input('What is the substractive method for colors?\na) CMYK\nb) RGB\nc) HSB\n')

if answer == 'a':
    points += 10
else:
    points -= 5

print('Your final score is:\n30/' + str(points))