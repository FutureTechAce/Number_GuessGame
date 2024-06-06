import random

randomNumber = random. randint(1, 20)
randomNumberHint = False
totalTries = 1
Guesses = 5
print("GUESS THE NUMBER! THE COMPUTER WILL GENERATE A RANDOM NUMBER BETWEEN 1 AND 20. YOU HAVE 6 TRIES TO GET IT RIGHT!")


while True:
        playerGuess = int(input("Enter A Number: "))
        if playerGuess > 20:
            print("Number is too high!")
        if playerGuess == randomNumber:
            print("Correct! You Guessed The Number Correctly!")
            break
        print("Total Tries: ",totalTries)
        if playerGuess != randomNumber:
            print("Wrong! ", Guesses,"Guesses Left!")
        totalTries +=1
        Guesses -=1
        if Guesses == 1:
            if randomNumber % 2 == 0:
                print("HINT! THE NUMBER IS EVEN")
            else:
                print("HINT! THE NUMBER IS ODD")
        if Guesses == 0:
            if playerGuess > randomNumber:
                print("NUMBER IS TOO HIGH!")
            else:
                print("NUMBER IS TOO LOW!")
        if Guesses == -1:
            print("You Lost! Out Of Tries! The Random Number Was ",randomNumber)
            break
