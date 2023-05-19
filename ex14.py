def convertList(list):
    result = []
    for item in list:
        if (item not in result):
            result.append(item)
    return result

list1 = ['Nate', 'Sujan', 'Jeff', 'Nate', 'Sujan']

def setFromList(list):
    return set(list)

print(list1)
print(convertList(list1))
print(setFromList(list1))
