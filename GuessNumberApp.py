import random as r

print('Welcome to Guess My Number App')
name = input('Hello!!, What is your name: ').title().strip()
print(f'Hi {name}, I thought of a number between 1 and 50')

randnum = r.randint(1, 50)
for i in range(8):
    guess = int(input('Take a guess: '))
    if guess < randnum:
        print('Number is too low. Choose a higher number.')
    elif guess > randnum:
        print('Number is too high. Choose a lower number.')
    else:
        break


if guess == randnum:
    print(f'You guessed it right in {i + 1} guesses . Hurrayyy')
else:
    print(f'Game over. The number I was thinking was {randnum}')