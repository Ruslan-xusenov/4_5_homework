from os import *
system("clear")

def kopaytirish(number):
    return "\n".join(f"{i} * {number} = {i * number}" for i in range(1, 11, 1))

print(kopaytirish(5))