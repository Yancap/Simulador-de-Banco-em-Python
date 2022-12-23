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
                cpf = str(input("Apenas 11 Dígitos inteiros!!!\nDigite um cpf válido >> "))
            elif cls.Autentication.validationCpf(cpf) == "notexist":
                break
        password = int(input("Digite sua senha (obs: apenas números inteiros) >> "))
        while True:
            if cls.Autentication.validationPassword(password) == "invalid":
                password = int(input("Digite uma senha válida >> "))
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
        
        cls.cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        while True:
            if cls.Autentication.validationCpf(cls.cpf) == "notexist":
                cls.cpf = str(input("CPF não existe em nossos bancos de dados!!!\nDigite um CPF existente >> "))
            elif cls.Autentication.validationCpf(cls.cpf) == "invalid":
                cls.cpf = str(input("Apenas 11 Dígitos inteiros!!!\nDigite um CPF válido >> "))
            elif cls.Autentication.validationCpf(cls.cpf) == "exist":
                break
        data = cls.Autentication.returnData(cls.cpf)[cls.cpf]
        
        cls.name = str(input("Digite seu Nome >> "))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationName(cls.name, "entrace", data)) == "exist":
                break
            else:
                print("Nome Inválido!\nVocê possui apenas", 4 - cls.Autentication.attempts,"Tentativas" )
                cls.name = str(input("Digite o Nome Correto >>"))
            
        cls.password = int(input("Digite Senha >> "))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationPassword(cls.password, "entrace", data)) == "exist":
                break
            else:
                print("Senha Inválido!\nVocê possui apenas", 4 - cls.Autentication.attempts,"Tentativas" )
                cls.password = int(input("Digite a Senha novamente >> "))

        cls.code = int(input("Digite seu Código de Segurança >> "))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationCode(cls.code, "entrace", data)) == "exist":
                break
            else:
                print("Código de Segurança Inválido!\nVocê possui apenas", 4 - cls.Autentication.attempts,"Tentativas" )
                cls.code = int(input("Digite a Código de Segurança novamente >> "))
        
        
        print("LOGIN EFETUADO COM SUCESSO!\nSeja Bem-Vindo(a)", cls.name)
        #Consertar a parte de operações
        

                

    @classmethod     
    def operationsMethod(cls): 
        
        while True:
            cls.dataPeople = cls.Autentication.returnData(cls.cpf)
            cls.operation = BankController.Operations(BankData(cls.cpf, cls.name, cls.password, cls.dataPeople[cls.cpf]["account"], cls.dataPeople[cls.cpf]["agency"], cls.code, cls.dataPeople[cls.cpf]["balance"]))
            os.system('cls') or None
            question = input("Qual operação que deseja fazer?\n 1- Saque\n 2- Deposito\n 3- Transferência\n 4- Ver Saldo Bancário\n 5- Sair\n\n>> ").lower()
            if question == "1" or question == "saque":
                os.system('cls') or None
                while True:
                    try:
                        value = float(input("Qual valor deseja sacar? \n>> "))
                        while cls.operation.withdraw(value) == "invalid":
                            value = float(input("Saldo Insuficiente!\nTente Novamente com outro Valor >> "))
                    except ValueError:
                        print("Digite apenas números")
                        continue
                    else:
                        break
                print("Operação realizada com sucesso!")
                os.system('cls') or None
                
            elif question == "deposito" or question == "2":
                os.system('cls') or None
                while True:
                    try:
                        value = int(input("Qual valor deseja depositar? \n>> "))
                    except ValueError:
                        print("Digite apenas números")
                    else:
                        cls.operation.deposit(value)
                        break
                print("Operação realizada com sucesso!")
                os.system('cls') or None
                
                
            elif question == "transferência" or question == "3":
                os.system('cls') or None
                
                
                while True:
                    try:
                        peopleAccount = int(input("Digite a Conta Bancaria em que deseja realizar a transferência >> "))
                        if cls.Autentication.validationAccount(peopleAccount) != "exist":
                            print("Digite uma Conta Bancaria existente!")
                            continue
                    except ValueError:
                        print("Digite apenas números")
                    else:
                        break
                

                while True:
                    try:
                        value = float(input("Qual valor deseja transferir? \n>> "))
                        while cls.operation.withdraw(value) == "invalid":
                            value = float(input("Saldo Insuficiente!\nTente Novamente com outro Valor >> "))
                    except ValueError:
                        print("Digite apenas números")
                        continue
                    else:
                        break

                cls.operation.transfer(cls.Autentication, peopleAccount, value)
                print("Valor Transferido com Sucesso!\n")    
                input("\nAperte ENTER para continuar >> ")
                os.system('cls') or None
                

            elif question == "ver saldo bancário" or question == "4":
                balance = cls.operation.getBankBalance()
                os.system('cls') or None
                print("Seu Saldo Bancário é: R$", balance)
                input("Aperte ENTER para continuar >> ")
            elif question == "sair" or question == "5":
                exit()
            else:
                pass
        return None

