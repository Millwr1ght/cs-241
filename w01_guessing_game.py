import random
from random import randint

#initiate
bool_replay = True
print('Welcome to the number guessing game!')
seed_value = input('Enter random seed: ')
random.seed(seed_value)

#begin game
while bool_replay == True:

    correct_answer = randint(1, 100)
    bool_gameplay = True
    guesses = 0
    while bool_gameplay == True:
        print()
        incorrect_answer = int(input('Please enter a guess: '))
        guesses += 1
        if incorrect_answer > correct_answer:
            #guess is bigger
            print('Lower')
        elif incorrect_answer < correct_answer:
            #guess is smaller
            print('Higher')
        else:
            #guess is not incorrect!!
            print('Congratulations. You guessed it!')
            print(f'It took you {guesses} guesses.\n')
            bool_gameplay = False

    #ask for a replay
    replay = input('Would you like to play again (yes/no)? ')
    if replay.lower() == 'n' or replay.lower() == 'no':
        #end game
        bool_replay = False
    #elif replay.lower() == 'y' or replay.lower() == 'yes':
        #play again
        #print('Let\'s play again!')
#end game
print('Thank you. Goodbye.')