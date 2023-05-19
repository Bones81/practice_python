# Password generator

import random as rd

# Need bank of letters, numbers, and symbols to pull from

symbols = '!@#$%^&?'
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'

options = [symbols, letters, numbers]

def genPW():
    def genPWOfLenX(desiredLength):
        password = []
        x = 0
        while (x < desiredLength):
            randOption = options[rd.randint(0, len(options) - 1)]
            randChar = randOption[rd.randint(0, len(randOption) - 1)]
            password.append(randChar)    
            x += 1
        return "".join(password)


    def getChoice():
        choice = input("How strong a password do you want: weak (w), medium (m), or strong (s): ").lower()
        if (choice != 'w' and choice != 'm' and choice != 's'):
            print("Please choose only (w)eak, (m)edium, or (s)trong: ")
            return getChoice()
        return choice
    
    choice = getChoice()

    if (choice == 'w'):
        wordBank = ['python', 'slithers', 'snakes', 'reptile', 'reticulated']
        randomIdx = rd.randint(0, len(wordBank)-1)
        def gen4RandDigits():
            digitsStr = []
            x = 0
            while(x < 4):
                digitsStr.append(str(rd.randint(0,9)))
                x += 1
            return "".join(digitsStr)
        password = wordBank[randomIdx] + gen4RandDigits()
        return password
    elif (choice == 'm'):
        return genPWOfLenX(8)
    else:
        return genPWOfLenX(20)
    
print(genPW())



    
            