from os import *
system("clear")

# Series 20
# n = 5
# raqamlar = [3, 1, 4, 2, 90]

# natija = []
# for i in range(n):
#     if i < n - 1:
#         a = min(raqamlar[i+1:])
#         natija.append(a)
#     else:
#         natija.append(None)

# print("To'plamning natijasi:",natija)

# Series 21

# n = 5
# numbers = [1, 2, 3, 4, 5]

# is_ascending = True
# for i in range(n - 1):
#     if numbers[i] > numbers[i + 1]:
#         is_ascending = False
#         break

# print("Natija:", is_ascending)


# Series 22
# n = 5
# raqamlar = [1, 2, 3, 4, 5]
# raqamlar = [5, 6, 8, 2, 1]
# osuvchi = True
# for i in range(n - 1):
#     if raqamlar[i] > raqamlar[i + 1]:
#         osuvchi = False
#         break

# print("Natija:", osuvchi)



# Series 23
# n = 5
# raqamlar = [2, 3, 1, 5, 4]

# def arra(q):
#     return (raqamlar[q - 1] < raqamlar[q + 1] or raqamlar[q] < raqamlar[q + 1])

# default_raqam = -1
# for i in range(1, n - 1):
#     if not arra(i):
#         default_raqam = i


# print("Dasturning natijasi:", default_raqam)



# Series 24

# n = 7
# raqamlar = [1, 0, 3, 4, 5, 0, 7]
# index = [i for i in range(n) if raqamlar[i] == 0]


# if len(index) < 2:
#     natija = 0
# else:
#     index_0 = index[-1]
#     index_2 = index[-2]
#     natija = sum(raqamlar[index_2 + 1:index_0])


# print("Dasturning natijasi:", natija)



# Series 25

""""
    Series 24 va Series 25 bir xil misol ekan
"""

# n = 7
# raqamlar = [0, 1, 3, 4, 5, 6, 0]
# index = [i for i in range(n) if raqamlar[i] == 0]


# if len(index) < 2:
#     natija = 0
# else:
#     index_0 = index[-1]
#     index_2 = index[-2]
#     natija = sum(raqamlar[index_2 + 1:index_0])


# print("Dasturning natijasi:", natija)



# Series 26


# n = 5
# raqamlar = [1, 2, 3, 4, 5]
# k = 3
# new_raqam = []

# for i in raqamlar:
    
#     new_raqam.append(i ** k)

# print("Dasturning natifasi:", new_raqam)



# Series 27


# n = 5
# numbers = [1, 2, 3, 4, 5]
# k = []
# a = 0

# for j in numbers:
#     a += 1
#     k.append(j ** a)


# print("Dasturning natijasi:", k)


# Series 28


# n = 6
# numbers = [1, 2, 3, 4, 5, 6]
# k = []
# a = 0

# for i in numbers:
#     n -= 1
#     k.append(i ** n)


# print("Dasturning natijasi:", k)



# Series 29

k = int(input("To'plamlarning sonini kiriting: "))
n = int(input("To'plamning sonlarini kiriting: "))

a = 0
for i in range(k):
    print(f'{i + 1}-to\'plamdagi {n} ta son kiriting: ')
    q = list(map(int, input().split()))
    a += sum(q)

print(f"Barcha sonlar yig'indisi: {a}" )