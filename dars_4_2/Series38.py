from os import *
system("clear")

def qwerty(k):
    r, a= [], 1
    while a != k + 1:
        d, b, c = True, 1, []
        while d:
            t = int(input(f"{a}-to'plamning {b}-elementini kiriting: "))
            c.append(t)
            b += 1
            if t == 0:
                d = False
        c.pop()
        y = sorted(c)
        if c == y:
            r.append(1)
        elif c == y[::-1]:
            r.append(-1)
        else:
            r.append(0)
        a += 1
    return r

print(qwerty(3))