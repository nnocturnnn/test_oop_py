

class CBookCard:
    def __init__(self, __name, __vidav, __kol, __tiraj, __rayt, __comment):
        self.__name = __name
        self.__vidav = __vidav
        self.__kol = __kol
        self.__tiraj = __tiraj
        self.__rayt = __rayt
        self.__comment = __comment
    
    def print(self):
        print(str(self.__name) + ' ' + str(self.__vidav)  + ' ' + str(self.__kol) + ' ' + 
        str(self.__comment) + "тираж: " + str(self.__tiraj) + "рейтинг :" + str(self.__rayt))
        
    
