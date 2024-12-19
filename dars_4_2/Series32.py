from os import *
system("clear")

k = int(input('To\'plamlar sonini kiriting: '))
add = 0
for i in range(k):
    lst = list(map(int, input(f"{i+1}-top'lamning elementlarini kiriting: ").split()))
    if 2 in lst:
        print(f"{i+1}-to'plamda 2 raqami topildi", lst)
    else:
        print(f"{i+1}-to'plamda 2 raqami topilmadi. Natija: 0")