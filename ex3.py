a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Look for numbers in list that are smaller than: '))

print([x for x in a if x < num])