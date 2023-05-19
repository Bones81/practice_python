def reverseString(lString):
    wordList = lString.split()
    revList = wordList[::-1]
    result = " ".join(revList)
    return result

longString = input("Enter a long string of words to reverse: ")
print(reverseString(longString))
