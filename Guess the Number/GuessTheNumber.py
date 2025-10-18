# Guess the Number
import random
number = random.randint(1,100)
print("Hi!, Welcome to the guess the number game")
while True:
    n=int(input("Enter your number what you are guessing between 1 to 100 >>> "))
    if number == n:
        print("Bingo, You Guess it Right!")
        break;
    elif n < number:
        print("Your number is small")
    else:
        print("Your number is large")
print("Game Over!")
