from os import *
system("clear")

k = int(input("To'plamlar sonini kiriting: "))

for i in range(k):
    lst = list(map(int, input(f"{i + 1}-to'plam elementlarini kiriting: ").split()))
    add = sum(lst)
    print(f"{i + 1}-to'plam yig'indisi:", add)