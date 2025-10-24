# Flip a coin

print("\n---*---Flip a coin---*---\n")

import random

def flipacoin(call):
    temp=random.randint(0,1)
    if temp == 0 and (call == 'H' or call == 'h'):
        return 'Its Head!,You Won the Toss!'
    elif temp == 1 and (call == 'T' or call == 't'):
        return 'Its Tail!,You Won the Toss!'
    else:
        return 'You loss the toss!'

print(flipacoin(input("Enter your call: H for head and T for tail!")))
