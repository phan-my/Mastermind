from random import randint

def nth_digit(x, nthDigit):
    return x//10**nthDigit % 10

digits = 3
health = 10
secret = randint(0, 10**(digits) - 1)
SecretArray = [0] * digits


guess = -1

while secret != guess: # NICHT while True
    guess = int(input("Guess the number: "))
    correctPosition = 0
    wrongPosition = 0
    chosenNumbers = [0] * 10
    
    for i in range(digits):
        SecretArray[i] = nth_digit(secret, i)
    
    for i in range(digits):
        for j in range(digits):
            # iterate through the array of the digits of guess and secret and compare the digits
            if nth_digit(guess, i) == nth_digit(secret, j):
                if nth_digit(secret, j) in SecretArray:
                    # correctPosition
                    if i == j:
                        correctPosition += 1
                    # wrongPosition
                    else:
                        wrongPosition += 1
                        
                    SecretArray[j] = -1

    
    # Problem: how to remember w duplicate numbers
    # (secret = 123; guess = 242; wrongPosition == 1)
    
    print("wrong position:", wrongPosition, "correct position:", correctPosition)
    # print(secret)
    
    if guess > 1000:
        print(secret)
        exit()
    
print("Correct!")
