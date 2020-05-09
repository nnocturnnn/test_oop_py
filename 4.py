class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell_about(self):
        print("Мене звуть - " + str(self.name) + ". Мені " + str(self.age) + " років.") 


class Buro(Human):
    def typen(self):
        self.type = "Бюрократ"

class Nefor(Human):
    def typen(self):
        self.type = "Неформал"

class Simple(Human):
    def typen(self):
        self.type = "Простак"

Andrey = Buro("Андрій", 30)
Roman = Nefor("Роман", 25)
Pavlo = Nefor("Павло",23)
Sergiy = Simple("Сергій", 32)
Iryna = Buro("Ірина",39)

listy = [Andrey, Roman, Pavlo, Sergiy, Iryna]

i = 0
k = 0
j = 0

while k < len(listy):
    print(listy[k].tell_about())
    k += 1

while j < len(listy) - 1:
    while i < len(listy) - j - 1: 
        if isinstance(listy[i], Buro):
            print(str(listy[i].name) + ': ' + "Доброго дня, " + str(listy[i + 1].name))
        elif isinstance(listy[i], Nefor):
            print(str(listy[i].name) + ': ' + "Привіт, " + str(listy[i + 1].name))
        elif isinstance(listy[i], Simple):
            if listy[i].age >= listy[i + 1].age:
                print(str(listy[i].name) + ': ' + "Привіт, " + str(listy[i + 1].name))
            else:
                print(str(listy[i].name) + ': ' + "Доброго дня, " + str(listy[i + 1].name))

        if isinstance(listy[i], Buro):
            print(str(listy[i + 1].name) + ': ' + "Доброго дня, " + str(listy[i].name))
        elif isinstance(listy[i], Nefor):
            print(str(listy[i + 1].name) + ': ' + "Привіт, " + str(listy[i].name))
        elif isinstance(listy[i], Simple):
            if listy[i + 1].age <= listy[i].age:
                print(str(listy[i].name) + ': ' + "Привіт, " + str(listy[i + 1].name))
            else:
                print(str(listy[i].name) + ': ' + "Доброго дня, " + str(listy[i + 1].name))
        i += 1
    j += 1
