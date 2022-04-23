import random
a = []
b = int(input("enter a number: "))
for i in range(b):
    n = 1
    while (random.randint(1,6)!=6):
        n += 1
    a.append(n)
print(sum(a)/len(a))
