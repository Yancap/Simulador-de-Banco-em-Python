from controller import BankController
from dal import BankDal
from model import BankData
import os


class BankView:
    
    Autentication = BankController.Validation()
        
    @classmethod
    def register(cls):
        
        print("----- REGISTRE-SE -----\n")
        name = input("Digite seu Nome Completo >> ")

        cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        while True:
            if cls.Autentication.validationCpf(cpf) == "exist":
                cpf = str(input("CPF EXISTENTE!!!\nDigite um cpf válido >> "))
            elif cls.Autentication.validationCpf(cpf) == "invalid":
                cpf = str(input("Apenas 11 Digitos inteiros!!!\nDigite um cpf válido >> "))
            elif cls.Autentication.validationCpf(cpf) == "notexist":
                break
        password = str(input("Digite sua senha (obs: apenas numeros inteiros) >> "))
        while True:
            if cls.Autentication.validationPassword(password) == "invalid":
                password = str(input("Digite uma senha válida >> "))
            else:
                break
            
        account = cls.Autentication.create("account")
        agency = cls.Autentication.create("agency")
        codeSecurity = cls.Autentication.create("code")

        BankDal.createData(BankData(cpf, name, password, account, agency, codeSecurity, 0))

        print("\n----- Registro Realizado com Sucesso -----\n")
        print("Esse são seus Dados...\n")
        print(" Conta Bancaria:", account)
        print(" Agencia Bancaria:", agency)
        print(" Código de Segurança:", codeSecurity)

    @classmethod
    def loginIn(cls):
        
        print("----- ENTRAR EM SUA CONTA -----\n")
        cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        while True:
            if cls.Autentication.autentication(validationCpf(cpf)) == "exist":
                break
            elif cls.Autentication.autentication(validationCpf(cpf)) == "notexist":
                print("CPF não exsitente!\nVocê possui", 3 - cls.Autentication.attempts, "Tentativas\n")
                cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
            elif cls.Autentication.autentication(validationCpf(cpf)) == "invalid":
                print("Digite apenas o CPF")
                cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
BankView().register()
