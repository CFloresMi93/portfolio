hour = int(input('Tell me what time is it and you will be answered with \ndifferent greetings depending on the time you have written\n'))

while True:

    if hour >= 0 and hour < 24:
        if hour < 6 or hour >= 21:
            print('Goodnight!')
        elif hour >= 6 and hour < 12:
            print('Good morning!')
        else:
            print('Good evening!')
        break
    else:
        print('It is not a possible time! Try again.')
        hour = int(input('What time is it?\n'))
