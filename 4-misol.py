from os import *
system("clear")

def shahar_ism(ism, shahar, davlat):
    toliq_ism = " ".join(ism)
    return f"Salom {toliq_ism}! {shahar}ning {davlat} shahriga xush kelibsiz !!!"

print(shahar_ism(["Ruslan", "Xusenov"], "O'zbekiston", "Toshkent"))