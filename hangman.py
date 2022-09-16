"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO:
    """
    x = N_TURNS
    current_world = ''
    ans = random_word()
    for i in range(len(ans)):
        current_world += '_'
    print('The words looks like ' + current_world)
    while True:
        guess = input('Guess a letter: ')
        if len(guess) != 1:
            print("illegal format.")
        elif not str.isalpha(guess):
            print("illegal format.")
        elif len(guess) == 1:
            guess = guess.upper()
            ok = False
            for i in range(len(ans)):
                if guess == ans[i]:
                    ok = True
                    test = ''
                    for j in range(len(ans)):
                        if i == j:
                            test += ans[j]
                        elif current_world[j].isalpha():
                            test += current_world[j]
                        else:
                            test += '_'
                    current_world = test
            if ok:
                print('You are right!')
                print('The words look like ' + current_world)
                print('You have ' + str(x) + ' wrong guess left.')
            else:
                if x == 1:
                    print('You are completely hung :(')
                    print('The word was ' + ans)
                    break
                else:
                    x -= 1
                    print("There is no "+guess+"'s "+'in the word.')
                    print('The words looks like '+current_world)
                    print('You have '+str(x)+' wrong guesses left.')
        if current_world == ans:
            print('You are correct!')
            print('You win!')
            print('The word is '+ans)
            break














def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
