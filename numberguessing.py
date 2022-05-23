import random as r

play = True
while play:

    def guess(x):
        random_number = r.randint(1,x)
        guess = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_number:
               print('Sorry, guess again. Try a little higher.')
            elif guess > random_number:
               print('Sorry, guess again. Try a little lower.')

        print(f'Congrats, you have guessed the correct number. It was {random_number}!')

    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = r.randint(low, high)
            else:
                guess = low # could also be high bc low=high
            feedback = input(f'Is {guess} too high (H), or too low (L), or correct (C)?'.lower())
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        print(f'Yay, the computer guessed your number,{guess}! ')
        reply = str(input("Play again? (Y or N) ").lower())
        if reply == "n":
            play = False

# computer_guess(100) for the computer to guess between 1 and 100
# guess(100) for the user to guess between 1 and 100