from os import *
system("clear")

a = int(input("To'plamning sonini kiriting: "))
r = []
i = 0
while a > i:
    i += 1
    k = []
    d = True
    while d:
        f = int(input("Son kiriting: "))
        if f == 0:
            d = False

        k.append(f)
    print(f"{i}-to'plam yaratildi")
    r.append(k)

    print([i[:-1] for i in r])