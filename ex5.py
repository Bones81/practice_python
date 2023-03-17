import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


rand_num1 = random.randint(10,20)
rand_num2 = random.randint(10,20)

c = []
for i in range(0,rand_num1):
    c.append(random.randint(0,50))

d = []
for i in range(0, rand_num2):
    d.append(random.randint(0,50))

common_els = []
for x in c:
    if x in d and x not in common_els:
        common_els.append(x)

print(common_els)
