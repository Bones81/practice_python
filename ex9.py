import random as rd

def finish():
        print(f'You made {guessCount} guesses. See you later.')
        exit()

secret = rd.randint(1,9)
print('Type "exit" at any prompt to finish the program.')

guessCount = 0

guess = input('I have selected a random integer between 1 and 9. Guess it!: ')
if (guess == 'exit'):
    finish()

guessCount += 1

while (int(guess) != secret):
    if(guess == 'exit'):
        finish()
    if(int(guess) > secret):
        guess = input('Try again. Your guess was too high.: ')
    else:
        guess = input('Try again. Your guess was too low.: ')
    guessCount += 1

print(f'You guessed the correct number: {secret}. It took you {guessCount} guesses.')