from phone import Phone

class Person():
    def __init__(self, name, cpf, age, phone):
        self.__name = name
        self.__cpf = cpf
        self.__age = age
        self.__phone = Phone(phone) # Letra maiúscula ?
        
# GET
    def getName(self):
        return self.__name
    
    def getCpf(self):
        return self.__cpf

    def getAge(self):
        return self.__age

    def getPhone(self):
        return self.__phone

# SET
    def setName(self, name):
        self.__name = name 
    
    def setCpf(self, cpf):
        self.__cpf = cpf
        
    def setAge(self, age):
        self.__age = age
    
    def setPhone(self, phone):
        self.__phone  = phone().setPhone(phone) 
          
person = Person()
person.getName()
    