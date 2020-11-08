#Zadanie 5

class Calculator:
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2

    def add(self):
        return self.liczba1 + self.liczba2

    def difference(self, odKtorej):
        if(odKtorej == 1):
            return self.liczba1 - self.liczba2
        else:
            return self.liczba2 - self.liczba1

    def multiply(self):
        return self.liczba1 * self.liczba2
    
    def divide(self, odKtorej):
        if(odKtorej == 1):
            return self.liczba1 / self.liczba2
        else:
            return self.liczba2 / self.liczba1


class ScienceCalculator(Calculator):
    def potegowanie(self, ktoraLiczba, potega):
        if(ktoraLiczba == 1):
            return self.liczba1 ** potega
        else:
            return self.liczba2 ** potega


kalkulator = Calculator(10, 20)
kalkNaukowy = ScienceCalculator(2, 3)

print(kalkulator.divide(2))
print(kalkNaukowy.potegowanie(2, 3))