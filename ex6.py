string = input('Please enter a string of letters to determine if it is a palindrome: ')

if string[::-1] == string:
    print('Yes, ' + string + ' is a palindrome.')
else:
    print('No, ' + string + ' is not a palindrome.')