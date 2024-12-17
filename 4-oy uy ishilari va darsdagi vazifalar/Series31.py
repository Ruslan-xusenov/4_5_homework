from os import *
system("clear")

k = int(input("To'plamlar sonini kiriting: "))

for i in range(k):
    lst = list(map(int, input(f"{i+1}-to'plamning elementlar sonini kiriting: ").split()))
    if 2 in lst:
        print(f"{i+1}-to'plamda 2 soni borligi aniqlandi: ", lst)
    else:
        print(f"{k} ta to'plamda 2 raqami aniqlanmadi")