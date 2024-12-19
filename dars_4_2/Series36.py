from os import *
system("clear")

a = int(input("To'plam sonini kiriting: "))

i = 0
k = []

while a > i:
    i += 1
    r = []
    d = True
    while d:
        f = int(input("Son kiriting: "))
        if f == 0:
            d = False
        r.append(f)
    print(f"{i}-to'plam yaratildi")
    k.append(r)

print([i[:-1] for i in k if sorted(i[:-1]) == i[:-1]])