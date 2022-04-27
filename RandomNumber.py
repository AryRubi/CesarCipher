#Guess the number minigame

#Guess the number between 1-10
#Enter number
#If wrong give hint and reduce 1 life
#Win = you guess it
#Lose = You ran out of lifes

import random

#Game process
def minigame():

    #number of lifes
    life = 3
    #primes list
    primes = [2, 3, 5, 7, 9]
    #random winning number from range
    win = random.randint(x, y)
    #multiple of the winning number for hint
    mult = random.randint(x, y)
    #random prime from the list
    prime = random.choice(primes)

    #loop for the game
    while True:

        print(' ')
        print('Enter your answer:')
        num = int(input(""))


        if num == win:
            print(' ')
            print('Congratulations! You WIN!')
            print(' ')
            break

        elif life == 3:
            print(' ')
            print("Sorry, wrong answer")
            print("Here is a hint: ")
            hint1 = win * win * win
            print(hint1, 'is the cubic power of the number')
            print(' ')
            life = 2
            continue

        elif life == 2:
            print(' ')
            print("Sorry, wrong answer")
            print("Here is a hint: ")
            hint2 = win * mult
            print(hint2, 'is a multiple of the number')
            print(' ')
            life = 1
            continue

        elif life == 1:
            print(' ')
            print("Sorry, wrong answer")
            print("Here is a hint: ")
            hint3 = win + prime
            print(hint3, "is the number added with a prime number")
            print(' ')
            life = 0
            continue

        elif life == 0:
            print(" ")
            print("GG bro, you LOSE.")
            print(" ")
            again = input("Play again? Yes/No ")
            again = again.lower()
            if again == "yes":
                life = 3
                print(" ")
                print('lifes restarted')
                win = random.randint(x, y)
                mult = random.randint(x, y)
                prime = random.choice(primes)
                continue
            elif again == "y":
                life = 3
                print(' ')
                print('lifes restarted')
                win = random.randint(x, y)
                mult = random.randint(x, y)
                prime = random.choice(primes)
                continue

            else:
                break

#number starting the range
x = 1
#number which the range finishes
y = 10
print(" ")
print("Guess the number: Enter a whole number from ", x,  " to ", y)
print("You get 4 lifes")

minigame()
