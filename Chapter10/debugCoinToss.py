#! python3

# debiggingCoinToss.py - debug program

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

import random

def main():
    guess = ''
    GUESSDIC = {0: 'tails', 1: 'heads'}

    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    logging.debug('GUESSDIC[toss] = %s' % (GUESSDIC[toss]))
    toss = GUESSDIC[toss]

    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
    return

if __name__ == '__main__': main()