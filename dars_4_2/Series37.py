from os import *
system("clear")

k = int(input("To'plamlar sonini kiriting: "))
i = 0

for i in range(k):
    print(f"{i+1}-to'plamning sonlarini kiriting: ")
    l = []

    while True:
        e = int(input())
        if e == 0:
            break
        l.append(e)
    

    if len(l) >= 2:
        osuvchi = True
        kamayuvchi = True

        for j in range(1, len(l)):
            if l[j] > l[j - 1]:
                kamayuvchi = False

            if l[j] < l[j - 1]:
                osuvchi = False

        
        if osuvchi or kamayuvchi:
            i += 1

print(f"O'suvchi yoki kamayuvchilar: {i}")