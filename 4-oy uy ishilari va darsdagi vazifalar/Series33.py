"""
    Series32 bilan bir xil ekan
"""
from os import *
system("clear")


k = int(input("To'plamlar sonini kirirting: "))

for i in range(k):
    lst = list(map(int, input(f"{i+1}-to'plamning elementlarini kiriting: ").split()))
    if 2 in lst:
        print(f"{i+1}-to'plamida 2 raqami aniqlandi")
    else:
        print(f"{i+1}-to'plamida 2 raqami aniqlanmadi. Natija: 0")