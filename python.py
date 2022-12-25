from random import *

number = (randint(1, 20))


guesses = 0

while guesses < 10:
    Guess = int(input())
    guesses += 1
    if Guess < number:
        print('Your guess is too low')
    if Guess > number:
        print('Your guess is yoo high')
    if Guess == number:
        break

if Guess == number:
    print('You guessed the number in ' + str(guesses) + ' tries!')

else:
    print('The number was ' + str(number))
