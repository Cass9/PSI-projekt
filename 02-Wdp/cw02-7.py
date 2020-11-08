#Zadanie 7

def odTylu(tekst):
    tekst2 = tekst[::-1]
    return "{} -> {}".format(tekst, tekst2)

print(odTylu("koteł"))

