from os import *
system("clear")

def mark_series(series):

    if series.endswith("!"):
        return series[:-1]
    return series

print(mark_series("Hi!"))
print(mark_series("Hi!!!"))