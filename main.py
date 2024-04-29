from random import randint

digits = 3
health = 10
secret = randint(0, 10**(digits) - 1)
guess = -1

while secret != guess: # NICHT while True
    guess = int(input("Guess the number: "))
    correct = 0
    
    # iteration and comparison
    for i in range(1, digits):
        if (secret//10**i) % 10 == (guess//10**i) % 10:
            correct += 1
    
    print(correct)
    # print(secret)
    
print("Correct!")