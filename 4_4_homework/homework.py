from os import *
system('clear')

# Series 14

# n = 5
# raqamlar = [1, 2, 3, 4, 5]

# add = sum(1 for raqam in raqamlar if raqam < 5)

# if add > 0:
#     print("Raqamlar:", add)
# else:
#     print(None)

# Series 15

# n = 6
# raqamlar = [3, 7, 2, 6, 9, 90]

# q = -1
# for i, raqam in enumerate(raqamlar):
#     if raqam > n:
#         q = i + 1
#         break

# if q != -1:
#     print(f"Dastur natijasi:", q)
# else:
#     print(0)

# Series 16

# n = 6
# raqamlar = [3, 2, 6, 6.1]

# q = -1
# for i, raqam in enumerate(raqamlar):
#     if raqam > n:
#         q = i + 1

# if q != -1:
#     print(f"Dastur natijasi:", q)
# else:
#     print(None)

# Series 17

# b = 20
# n = 3

# for q in range(n):
#     x = float(input(("Son kiriting: ")))
#     print(b + x)


# Series 18

# n = int(input("Sonni necha marta kiritmoqchisiz?: "))
# f = None
# t = True

# for q in range(n):
#     x = int(input("Sonni kiriting: "))
#     if x == f:
#         print(x)
#         e = True
#         print(f"Dublikat son topildi:", f)
#     f = x
# if not t:
#     print("Mavjud emas!")


# Series 19

# n = int(input("Sonlarni kiriting: "))
# q = None
# count = 0

# for i in range(n):
#     x = int(input("Sonni kiriting: "))
#     if q is not None and x < q:
#         count += 1
#     q = x
# print(count)