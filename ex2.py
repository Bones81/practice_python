num = int(input('Give me a number: '))
check = int(input('Give a number to divide by: '))
passes = (num % check) == 0

status = ('a multiple of ' + str(check)) if passes else 'not a multiple of ' + str(check)

msg = (f'{num} is {status}.')

print(msg)