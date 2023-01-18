import random

num = random.randint(1, 10)
myGuess = num
#print(myGuess)  # TODO delete

guess = int(input("Try to guess my number, it's between 1 and 10:\n"))

if guess == myGuess:
    print(f"Well done, you got it first try! \n my number is {myGuess}")

guesses = 1
while True:
    if guess == myGuess:
        print(f"You guessed it in {guesses} tries")
        break
    else:
        if guesses == 6:
            print("Sorry you loss, maybe you will have more luck next time")
            break
        elif guess < myGuess:
            print("Too low, please guess higher")
        elif guess > myGuess:
            print("Too high, Please guess lower")

        guesses += 1
        guess = int(input())