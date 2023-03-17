name = input('Give me your name: ')
print('Your name is ' + name)

age = input('Enter your age: ')
age = int(age)

current_year = int(input('Enter current year: '))

year_of_100 = current_year - age + 100

number_of_copies = int(input('Give me another number: '))

print('Printing ' + str(number_of_copies) + ' times: \n')
print((name + ', you will be 100 in ' + str(year_of_100) + '\n') * number_of_copies)


