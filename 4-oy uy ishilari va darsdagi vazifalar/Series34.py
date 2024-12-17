from os import *
system("clear")

k = int(input("To'plamlarning miqdorini kiriting: "))

for i in range(k):
    lst = list(map(int, input(f"{i+1}-toplamning elementlarini kiriting: ").split()))
    if 2 in lst:
        add = sum(lst)
        print(f"{i+1}-to'plamida 2 raqami topildi", add)
        add = sum(lst)