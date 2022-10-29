import random

random_num = random.randint(1, 10)

while True:
    print("guess a number 1 to 10:", end = " ")
    guessed_num = int(input())
    
    if guessed_num > random_num:
        print("guessed number is bigger. Try with smaller number!!")
    elif guessed_num < random_num:
        print("guessed number is smaller. Try with bigger number!!")
    elif guessed_num < 1 and guessed_num > 10:
        print("enter a valid number")
    else:
        print("U did it. A correct guess")
        break
