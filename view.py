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
        # cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        # while True:
        #     if cls.Autentication.autentication(cls.Autentication.validationCpf(cpf)) == "exist":
        #         break
        #     elif cls.Autentication.autentication(cls.Autentication.validationCpf(cpf)) == "notexist":
        #         print("CPF não exsitente!\nVocê possui", 3 - cls.Autentication.attempts, "Tentativas\n")
        #         cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        #     elif cls.Autentication.autentication(cls.Autentication.validationCpf(cpf)) == "invalid":
        #         print("Digite apenas o CPF")
        cpf = str(input("Digite seu CPF (obs: sem o '-') >> "))
        while True:
            if cls.Autentication.validationCpf(cpf) == "notexist":
                cpf = str(input("CPF não existe em nossos bancos de dados!!!\nDigite um cpf existente >> "))
            elif cls.Autentication.validationCpf(cpf) == "invalid":
                cpf = str(input("Apenas 11 Digitos inteiros!!!\nDigite um cpf válido >> "))
            elif cls.Autentication.validationCpf(cpf) == "exist":
                break
        
        name = str(input("Digite seu Nome >>"))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationName(name)) == "exist":
                break
            elif cls.Autentication.autentication(cls.Autentication.validationName(name)) == "notexist":
                print("Nome Inválido!\nVocê possui apenas", 3 - cls.Autentication.attempts,"Tentativas" )
                name = str(input("Digite o Nome Correto >>"))
            
        password = int(input("Digite Senha >>"))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationPassword(password)) == "exist":
                break
            elif cls.Autentication.autentication(cls.Autentication.validationPassword(password)) == "notexist":
                print("Senha Inválido!\nVocê possui apenas", 3 - cls.Autentication.attempts,"Tentativas" )
                password = int(input("Digite a Senha novamente >>"))

        code = int(input("Digite seu Codigo de Segurança >>"))
        while True:
            if cls.Autentication.autentication(cls.Autentication.validationCode(code)) == "exist":
                break
            elif cls.Autentication.autentication(cls.Autentication.validationCode(code)) == "notexist":
                print("Codigo de Segurança Inválido!\nVocê possui apenas", 3 - cls.Autentication.attempts,"Tentativas" )
                code = int(input("Digite a Codigo de Segurança novamente >>"))
        
        cls.dataPeople = cls.Autentication.returnData(cpf)
        print("LOGIN EFETUADO COM SUCESSO!\nSeja Bem-Vindo(a)", name)
        #Consertar a parte de operações
        cls.operation = BankController.Operations(cpf, name, password, cls.dataPeople[cpf]["account"], cls.dataPeople[cpf]["agency"], code, cls.dataPeople[cpf]["balance"])
        cls.operationsMethod(cls.operation)
        @classmethod     
        def operationsMethod(cls, accountPeople: BankController.Operations): 
            
            while True:
                os.system('cls') or None
                question = input("Qual operação que deseja fazer?\n 1- Saque\n 2- Deposito\n 3- Transferencia\n 4- Ver Saldo Bancario\n 5- Sair\n\n>> ").lower()
                if question == "1" or question == "saque":
                    os.system('cls') or None
                    while True:
                        try:
                            value = float(input("Qual valor deseja sacar? \n>> "))
                            while accountPeople.withdraw(value) == "invalid":
                                value = float(input("Saldo Insuficiente!\nTente Novamente com outro Valor >> "))
                        except ValueError:
                            print("Digite apenas numeros")
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
                            print("Digite apenas numeros")
                        else:
                            accountPeople.deposit(value)
                            break
                    print("Operação realizada com sucesso!")
                    os.system('cls') or None
                    
                    
                elif question == "transferencia" or question == "3":
                    os.system('cls') or None
                    
                    
                    while True:
                        try:
                            peopleAccount = int(input("Digite a Conta Bancaria em que deseja realizar a transferencia >> "))
                            if cls.Autentication.validationAccount(peopleAccount) != "exist":
                                print("Digite uma Conta Bancaria existente!")
                                continue
                        except ValueError:
                            print("Digite apenas numeros")
                        else:
                            break
                    while True:
                        try:
                            peopleAgency = int(input("Digite a Agencia em que deseja realizar a transferencia >> "))
                            if cls.Autentication.validationAgency(peopleAgency) != "exist":
                                print("Digite uma Agencia Bancaria existente!")
                                continue
                        except ValueError:
                            print("Digite apenas numeros")
                        else:
                            break

                    while True:
                        try:
                            value = float(input("Qual valor deseja transferir? \n>> "))
                            while accountPeople.withdraw(value) == "invalid":
                                value = float(input("Saldo Insuficiente!\nTente Novamente com outro Valor >> "))
                        except ValueError:
                            print("Digite apenas numeros")
                            continue
                        else:
                            break

                    accountPeople.transfer(cls.Autentication, peopleAccount, value)
                    print("Valor Transferido com Sucesso!\n")    
                    input("\nAperte ENTER para continuar >> ")
                    os.system('cls') or None
                    

                elif question == "ver saldo bancario" or question == "4":
                    accountPeople.getBankBalance()
                    os.system('cls') or None
                elif question == "sair" or question == "5":
                    exit()
                else:
                    pass
            return None
BankView().loginIn()
