from os import *
system("clear")

def letter(s):
    if s:
        return s[0].upper() + s[1:]
    return s

print(letter("Hello"))
print(letter("hello"))
print(letter("a"))
print(letter(" "))
print(letter("1q"))