def reverseString(lString):
    wordList = lString.split()
    print(wordList)

    revList = wordList[::-1]
    print(revList)

    result = " ".join(revList)
    print(result)

    return result

longString = "Hello world, my name is Nathan, and I am a software engineer."

reverseString(longString)
