from math import pi


def pole(czyKolo, a=0, b=0, h=0) -> float:
    if (czyKolo == True and a > 0):
        return a * a * pi
    elif (a > 0 and b > 0 and h > 0):
        return (((a + b) * h) / 2)
    elif (a > 0 and b > 0):
        return a * b
    elif (a > 0):
        return a ** 2
    else:
        print("wprowadzono błędne dane")
        return -1
