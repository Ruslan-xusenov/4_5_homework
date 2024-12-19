from os import *
system("clear")


n = 5
raqamlar = [3, 1, 4, 2, 90]
# 
natija = []
for i in range(n):
    if i < n - 1:
        a = min(raqamlar[i+1:])
        natija.append(a)
    else:
        natija.append(None)

print("To'plamning natijasi:",natija)