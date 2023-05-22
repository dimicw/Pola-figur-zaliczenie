from math import pi

# funkcja obliczająca pole figury na podstawie parametrów
def pole(czyKolo, a=0, b=0, h=0) -> float:
    if (czyKolo == True and a > 0):     # jeśli figura to koło
        return a * a * pi
    elif (a > 0 and b > 0 and h > 0):   # jeśli figura to trapez
        return (((a + b) * h) / 2)
    elif (a > 0 and b > 0):             # jeśli figura to prostokąt
        return a * b
    elif (a > 0):                       # jeśli figura to kwadrat
        return a ** 2
    else:
        print("wprowadzono błędne dane")    # wyświtlenie komunikatu o błędzie, kiedy figura nie spełnia warunków
        return -1       # zwrócenie wartości -1 jako oznaczenia błędu
