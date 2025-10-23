# Rock paper Scissor

import random,sys

print('\n---*---ROCK, PAPER, SCISSORS---*---\n')
Win = 0
Loss = 0
Tie = 0

while True:
    print("Enter your move: r for Rock, s for Scissor and p for paper or q to Quit the Game")
    move =input(">>>")
    if move == 'q' or move == 'Q':
        sys.exit()
    elif move == 'r'or move =='R':
        print("Rock vs ...")
    elif move == 's' or move == 'S':
        print("Scissor vs ...")
    elif move == 'p' or move =='P':
        print("Paper vs ...")
    else:
        print("invalid input")
        continue
    temp = random.randint(1,3)
    if temp == 1:
        print("Rock")
    elif temp == 2:
        print("Scissor")
    elif temp ==3:
        print("Paper")
    if (move  =='r' or move == 'R') and temp == 1 :
        print("Its Tie!")
        Tie+=1
    elif (move  =='r' or move == 'R') and temp ==2  :
        print("You Won!")
        Win+=1
    elif (move  =='r' or move == 'R') and temp ==3 :
        print("You Loss!")
        Loss+=1
    elif (move  =='s' or move =='S') and temp ==1 :
        print("You Loss!")
        Loss+=1
    elif (move  =='s' or move =='S') and temp ==2 :
        print("Its Tie!")
        Tie+=1
    elif (move  =='s' or move =='S') and temp ==3 :
        print("You Won!")
        Win+=1
    elif (move  =='p' or move == 'P') and temp ==1 :
        print("You Won!")
        Win+=1
    elif (move  =='p' or move == 'P') and temp ==2 :
        print("You Loss!")
        Loss+=1
    elif (move  =='p' or move == 'P') and temp ==3 :
        print("Its Tie!")
        Tie+=1
    print("Win:",Win, "Loss:",Loss, "Tie:",Tie)








