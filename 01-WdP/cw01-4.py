#Zadanie 4
zmienna_typu_string = "wstawiam tu cos"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.join)
print("Przykład z join")
print(",".join(['jan', 'kowalski', 'lat', '2']))

#Zadanie 5
imie = "Piotr"
naz = "Mierzejewski"

print("{} {}".format(imie[::-1].capitalize(), naz[::-1].capitalize()))

#Zadanie 6
lista = list(range(1,11))
lista2 = lista[5:10]
lista = lista[0:5]
print(lista)
print(lista2)

#Zadanie 7
lista.extend(lista2)
print(lista)

lista.insert(0, 0)
print(lista)

