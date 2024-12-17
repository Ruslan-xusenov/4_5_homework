from os import *
system('clear')
# 1-misol

# def ishchi_ichimliklari(ishchilar):
#     ichimliklar = {
#         "Jabroni":	        "Patron Tequila",
#         "School Counselor":	"Anything with Alcohol",
#         "Programmer":	    "Hipster Craft Beer",
#         "Bike Gang Member":	"Moonshine",
#         "Politician":	    "Your tax dollars",
#         "Rapper":	        "Cristal",
#         "fuotball":         "Beer"
#     }
#     ishchilar = ishchilar.lower()

#     return ichimliklar.get(ishchilar, "Pivo")


# print(ishchi_ichimliklari("Jabroni"))
# print(ishchi_ichimliklari("School Counselor"))
# print(ishchi_ichimliklari("Programmer"))
# print(ishchi_ichimliklari("Bike Gang Member"))
# print(ishchi_ichimliklari("Politician"))
# print(ishchi_ichimliklari("Rapper"))
# print(ishchi_ichimliklari("Foutball"))


# 2-misol

# def raqamlar(s):
#     if not s or s.count(',') <= 1:
#         return None
    
#     elementlar = s.split(',')

#     return ' '.join(elementlar[1:-1])


# print(raqamlar("1,2,3"))
# print(raqamlar("1,2,3,4"))
# print(raqamlar("1,2,3,4,5"))
# print(raqamlar(""))
# print(raqamlar("1"))
# print(raqamlar("1,2"))


# 3-misol


# def dollar(sent):
#     return "${:.2f}".format(sent)

# print(dollar(3))
# print(dollar(3.1))


# 4-misol
# import re

# def remove(text):
#     return re.sub(r'd', '', text)

# print(remove("! !"))
# print(remove("123456789"))
# print(remove("This Looks5 Great"))

# 5-misol

# def sor(strings):
#     string_1 = sorted(strings)[0]
#     return '***'.join(string_1)

# print(sor("apple"))


""""
    METOD OVERRIDE
"""

# 1-misol
# class Animals:
#     def speak(self):
#         return "Hayvonlar o'zlarining tovushlariga ega!!!"
    

# class Dog(Animals):
#     def speak(self):
#         return "Woof, woof"
    

# hayvonlar = Animals()
# it = Dog()

# print(hayvonlar.speak())
# print(it.speak())

"""
    ATRIBUT OVERRIDE
"""

# class Klaviatura:
#     mexanik = "Tik, tik"


# class Klaviatura_1(Klaviatura):
#     membrana = "Chris, chris"


# mexanik_1 = Klaviatura()
# membrana_1 = Klaviatura_1()

# print(mexanik_1.mexanik)
# print(membrana_1.membrana)