from doctor import Doctor
from lawyer import Lawyer

doctorList = []
lawyerList = []
#                          crm      nome      cpf       telefone
FirstPersonDoctor = Doctor(123456, 'Gustavo', 24787839, 243903)
SecondPersonDoctor = Doctor(12321, 'Adwaita', 23434223, 234444)

doctorList.append(FirstPersonDoctor)
doctorList.append(SecondPersonDoctor)

#                          oab    name     cpf     telefone
FirstPersonLawyer = Lawyer(2343, 'Hector', 345435, 5435534)
SecondPersonLawyer = Lawyer(2345, 'Ricardo', 1233, 3213213)

lawyerList.append(FirstPersonLawyer)
lawyerList.append(SecondPersonLawyer)

for law in lawyerList:
    print('OAB: {} | NAME: {} | AGE: {}'.format(law.getOab(), law.getName(), law.getAge()))
    print('CPF: {} | PHONE: {}'.format(law.getCpf(), law.getPhone().getPhone()))
    
for med in doctorList:
    print('CRM: {} | NAME: {} | AGE: {}'.format(med.getOab(), med.getName(), med.getAge()))
    print('CPF: {} | PHONE: {}'.format(med.getCpf(), med.getPhone().medPhone()))
    
