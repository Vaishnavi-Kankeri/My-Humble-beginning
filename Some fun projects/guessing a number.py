guess = 0
tries = 0

while guess != 6:
    try:
        guess = int(input('Guess the number: '))
    except ValueError:
        print('Please enter a valid number! ')
        continue
        
    tries += 1
    if guess < 6:
         print('Too low!')
    elif guess > 6:
        print('Too high!')
    
    if tries == 5:
        print('lol! You are out of tries')
        break

if guess == 6:
        print('You have guessed it right!')
