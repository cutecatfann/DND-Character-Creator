from random import randint

def rollDie(count, size):
    ''' Simple DnD die roller. Gets the number of dice to roll and the number of sides on the die'''
    dice = []
    for i in range(count):
        dice.append(randint(1, size))
    return dice

