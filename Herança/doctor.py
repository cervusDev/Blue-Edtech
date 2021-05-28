from person import Person
class Doctor(Person):
    def __init__(self, name, cpf, age, phone, crm):
        self.__crm = crm
        super().__init__(name, cpf, age, phone)
        
#GET
    def getCrm(self):
        return self.__crm
#SET
    def setCrm(self, crm):
        self.__crm = crm
