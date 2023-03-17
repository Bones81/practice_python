#ask for num then print out all divisors of that num
num=int(input('Give me a number: '))

pos_divisors = range(1, num + 1)

result = []
for n in pos_divisors:
    if num % n == 0:
        print(n)
