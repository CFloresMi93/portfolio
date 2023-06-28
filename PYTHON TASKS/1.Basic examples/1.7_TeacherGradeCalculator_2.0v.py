'''This program will calculate the average of three exam grades, which are
the 60% of global calification, and three tasks grades, which are the 40%
of global calification'''

maths = int(input('What is your mark in maths exam?'))
history = int(input('What is your mark in history exam?'))
spanish = int(input('What is your mark in spanish exam?'))

mathTask = int(input('What is your mark in maths task?'))
historyTask = int(input('What is your mark in history task?'))
spanishTask = int(input('What is your mark in spanish task?'))

average = ((maths + history + spanish) / 3) * 0.6 + ((mathTask + historyTask + spanishTask) / 3) * 0.4

print('The average of these grades is ' + str(average))