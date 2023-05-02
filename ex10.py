import random

a = list(random.randint(1,99) for i in range(1, random.randint(10,20)))
b = random.sample(range(100), 15)
c = []

if (len(a) > len(b)):
    for i in a:
        if(i in b and i not in c):
            c.append(i)
else:
    for i in b:
        if (i in a and i not in c):
            c.append(i)

a.sort()
b.sort()
c.sort()

print(a)
print(b)
print(c)
