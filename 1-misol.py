from os import *
system("clear")


def  soz_qaytar(soz):
    soz_1 = soz.split()

    takror = soz_1[::-1]

    return " ".join(takror)

print(soz_qaytar("Xusenov Ruslan"))
print(soz_qaytar("O'roqov Ketmon"))