#!/usr/bin/python3

import random

if __name__ == '__main__':
    print("Let's Play Rock, Paper, Scissors")
    computerlist = ['R', 'P', 'S']
    win = tie = lose = 0
    while True:
        oppchoice = random.choice(computerlist)
        action = input("Choose [R]ock, [P]aper, or [S]cissors : ").upper()
        if action not in "RPS" or len(action) != 1:
            print("Not a valid choice.")
        if action == oppchoice:
            tie += 1
            print("You Tied! :-| Current Wins-Losses-Ties: {}-{}-{}".format(win, lose, tie))
        if (action == 'R' and oppchoice == 'S') or (action == 'P' and oppchoice == 'R') or (
                action == 'S' and oppchoice == 'P'):
            win += 1
            print("You Win! :-) Current Wins-Losses-Ties: {}-{}-{}".format(win, lose, tie))
        if (action == 'R' and oppchoice == 'P') or (action == 'P' and oppchoice == 'S') or (
                action == 'S' and oppchoice == 'R'):
            lose += 1
            print("You Lose :-( Current Wins-Losses-Ties: {}-{}-{}".format(win, lose, tie))
