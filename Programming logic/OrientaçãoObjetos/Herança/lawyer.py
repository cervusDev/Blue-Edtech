from person import Person

class Lawyer(Person):
    def __init__(self, oab, name, cpf, age, phone):
        self.__oab = oab
#                       palavra reservada 'super().__init__()', para gerar a herança da classe Person
        super().__init__(name, cpf, age, phone)

# GET
    def getOab(self):
        return self.__oab
    
# SET
    def setOab(self, oab):
        self.__oab = oab