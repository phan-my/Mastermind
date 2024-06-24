from random import randint

# e.g. nth_digit(98765, 3) == 8
def nth_digit(x, nthDigit):
    return (x//(10**nthDigit)) % 10

digits = 3
secret = randint(0, 10**(digits) - 1) # [000, 999]
SecretArray = [0] * digits # same as secret but as array, 1234 -> [4, 3, 2, 1]
GuessArray = [0] * digits
guess = -1

while secret != guess: # NICHT while True
    guess = int(input("Guess the number: "))
    correctPosition = 0
    wrongPosition = 0
    
    # (re)set SecretArray
    for i in range(digits):
        SecretArray[i] = nth_digit(secret, i)
        GuessArray[i] = nth_digit(guess, i)
    
    if guess > 10**digits:
        print("Game over. Secret:", secret)
        break
    
    # checking correctPosition
    # if position match, correctPosition++ and rm that _number_
    #from SecretArray
    for i in range(digits):
        if GuessArray[i] == SecretArray[i]:
            correctPosition += 1
            SecretArray[i] = -1
            GuessArray[i] = -2
            # print("rm Secretarray[", i, "] = ", SecretArray[i])

    
    # checking wrongPosition
    # iterate 2nd time because wrongPosition has lower priority (to avoid
    #collisions with correctPostion above); note the i != j , where i is index
    #for guess and j is index for secret
    for i in range(digits):
        for j in range(digits):
            if GuessArray[i] == SecretArray[j] and GuessArray[i] in SecretArray:
                if i != j:
                    """
                    print("wrong. guess:", nth_digit(guess, i), "; i:", i)
                    print("     . secret:", nth_digit(secret, j), "; j:", j)
                    """
                    wrongPosition += 1
                    GuessArray[i] = -2
                    SecretArray[j] = -1
                    break
   
    print (
        "wrong position:", wrongPosition,
        "correct position:", correctPosition, "\n"
    )
    
    
    """
    # print(secret)
    
    
    if guess > 1000:
        print(secret)
        exit()
    """
    
print("Correct!")