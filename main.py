from random import randint

# e.g. nth_digit(98765, 3) == 8
def nth_digit(x, nthDigit):
    return x//(10**nthDigit) % 10

digits = 3
secret = randint(0, 10**(digits) - 1) # [000, 999]
SecretArray = [0] * digits # same as secret but as array, 1234 -> [4, 3, 2, 1]
guess = -1

while secret != guess: # NICHT while True
    guess = int(input("Guess the number: "))
    correctPosition = 0
    wrongPosition = 0
    
    # (re)set SecretArray
    for i in range(digits):
        SecretArray[i] = nth_digit(secret, i)
        
    """ Bug
    secret == 118:
        guess == 111 -> wrongPosition == 2, correctPosition == 1
        guess == 181 -> wrongPosition == 3, correctPosition == 0
        guess == 118 -> "Correct!", wrongPosition == 1, correctPosition == 2
    secret == 454:
        guess == 444 -> wrongPosition == 1, correctPosition == 1
        guess == 454 -> wrongPosition == 1, correctPosition == 1
    secret == 695:
        guess = 695 -> wrongPosition == 0, correctPosition == 1
    """
    
    # checking correctPosition
    # if position match, correctPosition++ and rm that _number_
    #from SecretArray
    for i in range(digits):
        if nth_digit(guess, i) == nth_digit(secret, i) and \
        nth_digit(guess, i) in SecretArray:
            correctPosition += 1
            SecretArray[i] = -1
            break
    
    # checking wrongPosition
    # iterate 2nd time because wrongPosition has lower priority (to avoid
    #collisions with correctPostion above); note the i != j , where i is index
    #for guess and j is index for secret
    for i in range(digits):
        for j in range(digits):
            if nth_digit(guess, i) == nth_digit(secret, j) and \
               nth_digit(secret, j) in SecretArray:
                if i != j:
                    wrongPosition += 1
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