#import the random module
from random import randint
#set a variable to hold the random number 1-9
#chose a smaller number because it was easier to test
randomNumber=randint(0,9)
#instantiate guess
guess =0
print('Welcome to the guessing game...Guess a random number 1-9')
#goes through the users guesses
while guess != randomNumber:
    guess = input()
    guess = int(guess)
    #tells the user to guess higher or lower based on their guess
    if guess > randomNumber:
        print('Your guess is too high. Please guess again!')
    elif guess < randomNumber:
         print('Your guess is too low. Please guess again!')
    else:
        print('You are correct!')
        break