from random import randint

digits = 5
health = 10
secret = randint(0, 10**(digits) - 1)

while True:
    guess = int(input("Guess the number: "))
    correct = 0
    
    if secret == guess:
        print("Correct!")
        break
    
    # iteration and comparison
    for i in range(1, digits+1):
        if (secret//10**i) % 10 == (guess//10**i) % 10:
            correct += 1
    
    print(correct)
