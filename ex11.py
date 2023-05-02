chosenNum = int(input('Give me a number: '))


def isPrime(num):
    possible_divisors = range(2, int(num / 2) + 1) 
    
    # we want to check all possible factors from 2 through num / 2. After that, the only possible factor will be the num itself, so if none of the possible factors in this range leave a remainder of 0, we have a prime number. 

    for i in possible_divisors:
        if (num % i == 0):
            return False
    
    return True

result = isPrime(chosenNum)

if (result):
    print(f'{chosenNum} is a prime number!')
else:
    print(f'{chosenNum} is not a prime number.')
