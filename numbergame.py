from random import randint;

def numgame():

    randNum = randint(1, 100)
    guessNum = 0
    print('Welcome to the number game!')
    while guessNum != randNum:
        guessNum = int(input('Please enter a guess between 1 and 100: '))
        if (guessNum == randNum):
            print('Correct')
            break
        elif (guessNum > randNum):
            print('Too high')
        else:
            print('Too low')