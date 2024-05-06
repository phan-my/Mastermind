from random import randint

digits = 3
health = 10
secret = randint(0, 10**(digits) - 1)
guess = -1

while secret != guess: # NICHT while True
    guess = int(input("Guess the number: "))
    correctPosition = 0
    
    # iteration and comparison
    # BUG for secret = 189, we have 999 that does not register
    for i in range(0, digits):
        if (secret//(10**i)) % 10 == (guess//(10**i)) % 10:
            correctPosition += 1
    
    # Problem: how to remember w duplicate numbers
    # (secret = 123; guess = 242; correctNumber == 1)
    
    print(correctPosition)
    # print(secret)
    
print("Correct!")
