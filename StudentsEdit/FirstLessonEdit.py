import random

num = random.randint(1, 5)
myGuess = num
#print(myGuess)  # TODO delete

guess = int(input("GOODLUCK MF HAHAHHA GUSSE MA NUMBERRRR\n"))

if guess == myGuess:
    print(f"BROOO YOU ONLY GOT IT BC I WANTED YOU TO WIN THIS IS WHATEVER IT IS \n my number is {myGuess}")

guesses = 1
while True:
    if guess == myGuess:
        print(f"SO WHAT IF YOU WON BC IT AINT ON FIRST TRY LMAO MF YOU NEEDED {guesses} TRIES HAHHAHAH!!!")
        break
    else:
        if guesses == 3:
            print("HAHHHHH I KNEW IT YOU BAKAA YOU CANT GUSSE IT ")
            break
        elif guess < myGuess:
            print("PFFFT DO YOU EVEN TRY!")
        elif guess > myGuess:
            print("LOSERRR!")

        guesses += 1
        guess = int(input())