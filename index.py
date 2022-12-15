import random
import json
import os
#comentar cada sessão
class Bank():
    __dataBank = []
    __dataComplete = []
    __cpf = []
    def __init__(self, digit):

        #Função que cria a Conta Bancaria, Agency e o Codigo de Segurança e impede sua duplicação, também recebe a senha e o cpf.
        #Essa função tambem verifica se o CPF é valido ou se ja existe no banco de dados.
        def create(index):
            dataX = open("data.txt", "r", encoding="UTF-8")
            dataX = dataX.readlines()
            dataCpf = []
            dataMain = []
            for data in dataX:
                for i in json.loads("{"+data+"}").values():
                    dataMain.append(i)
                dataCpf += json.loads("{"+data+"}").keys()
            
            if index == 1:
                #Conta Bancaria com 00000-0
                while True:
                    aux = 0
                    randomNum = random.randint(100000,999999)
                    for data in dataMain:
                        if data['account'] == randomNum:
                            break
                        else:
                            aux += 1
                    if len(dataMain) == aux:
                        return randomNum

            elif index == 2:
                #Agencia com 4 digitos: 0000
                while True:
                    aux = 0
                    randomNum = random.randint(1000,9999)
                    for data in dataMain:
                        if data['agency'] == randomNum:
                            break
                        else:
                            aux += 1
                    if len(dataMain) == aux:
                        return randomNum
                
            elif index == 3:

                    try:
                        password = int(input("Digite sua senha\n(obs: 5 caracteres):"))
                        while password < 10000 or password > 99999:
                             password = int(input("Digite apenas 5 numeros:"))
                    except ValueError:
                        while True:
                            try:
                                password = int(input("Digite apenas numeros: "))
                                while password < 10000 or password > 99999:
                                    password = int(input("Digite apenas 5 numeros:"))
                            except ValueError:
                                continue
                    return password
            elif index == 4:
                try:
                    cpf = int(input("Digite seu CPF\n(obs: digite sem o '-'): "))
                    while cpf < 10000000000 or cpf > 99999999999 or str(cpf) in dataCpf:
                            cpf = int(input("Digite um CPF valido: "))
                except ValueError:
                    while True:
                        try:
                            cpf = int(input("Digite apenas numeros: "))
                            while cpf < 10000000000 or cpf > 99999999999 or str(cpf) in dataCpf:
                                cpf = int(input("Digite digite um CPF valido: "))
                        except ValueError:
                            continue
                        else:
                            break
                
                return cpf
            else:
                
                while True:
                    aux = 0
                    randomNum = random.randint(1000,9999)
                    for data in dataMain:
                        if data['codeSecurity'] == randomNum:
                            break
                        else:
                            aux += 1
                    if len(dataMain) == aux:
                        return randomNum
                

        
        #------------------------------------ Criação de Contas -------------------
        if digit == 2:
            
            #------------------ Entrada de Dados ----------------
            name = str(input("Digite seu Nome: "))
            cpf = create(4)
            account = create(1)
            agency = create(2)
            password = create(3)
            codeSecurity = create(5)

            #--------------- Gera o Banco de Dados E Salva as Informações --------------
            data = open("data.txt", "a", encoding="UTF-8")
            self.__dataString = json.dumps(str(cpf))+ ":" + "{" + '"name"' + ":" + json.dumps(name).lower() + "," + '"account"' + ":" + json.dumps(account) + "," + '"agency"' + ":" + json.dumps(agency) + "," + '"password"' + ":" + json.dumps(password) + "," + '"codeSecurity"' + ":" + json.dumps(codeSecurity) + "," + '"balance"' + ":" + json.dumps(0.0) + "}"+"\n"
            data.write(self.__dataString)
            data.close()
            
            data = open("data.txt", "r", encoding="UTF-8")
            auxData = data.readlines()
            self.__dataBank = auxData
            newData = "{"
            for i in auxData:
                for j in i:
                    if j == "'" or j == "\n":
                        pass
                    if j == "}":
                        newData += j + ","
                        continue
                    newData += j
            
            newData = newData[:-2] + "}"

            #-------------- Apresentação das Informações ---------------
            print("Gerando Dados...\n")
            print(" Sua Conta Bancaria é:", account)
            print(" Sua Agencia é:", agency)
            print(" Seu Código de Segurança é:", codeSecurity)
            input("\nAperte ENTER para continuar >> ")
            os.system('cls') or None
            data.close()

            #------- Função de Login ------------
            self.login()
        else:
            self.login()
        #-------- Inicio das operações ----------   
        self.operations()

    #---------------------------- ENTRAR NA CONTA ---------------------------------
    def login(self):

        #----- Função que autentica cada etapa login, cada dado digitado --------
        def autentication(data, tp):
            #Estrutura da Funçao:   Caso os dados digitados passem pela autenticação, a função da continuidade e retorna o dado digitado
            #Caso os dados não passem pela autenticação, o usuario terá 3 tentativas, caso esgotada, o seu acesso será bloqueado e o programa fechará
            i = 0
            if tp == 'name':
                name = input("Digite seu Nome: ").lower()
                while i < 3:
                    if name == data["name"]:
                        break
                    else:
                        i += 1
                        if i < 3 :
                            print("Você possui apenas", 3-i, "tentativas")
                            name = input("Digite seu Nome Novamente: ").lower()
                            continue
                        else:
                            self.block()
                return name.lower()

            elif tp == 'account': 
                while True:
                    try:
                        account = int(input("Digite sua Conta Bancaria: (obs: 6 digitos) >> "))
                        while account < 100000 or account > 999999:
                                account = int(input("Apenas 6 Digitos \nDigite sua Bancaria: (obs: 6 digitos) >> "))
                    except ValueError:
                        print("Digite apenas numeros inteiros")
                        continue
                    else:
                        
                        
                        i = 0
                        while i < 3:
                            if account == data['account']:
                                break
                            else:
                                i += 1
                                if i < 3 :
                                    print("Você possui apenas", 3-i, "tentativas")
                                    account = int(input("Digite sua Bancaria Novamente: (obs: 6 digitos) >> "))
                                    continue
                                else:
                                    self.block()
                            
                        break
                return account

            elif tp == 'agency':
                while True:
                    try:
                        agency = int(input("Digite sua Agencia: (obs: 4 digitos) >> "))
                        while agency < 1000 or agency > 9999:
                                agency = int(input("Apenas 4 Digitos \nDigite sua Agencia: (obs: 4 digitos) >> "))
                    except ValueError:
                        print("Digite apenas numeros inteiros")
                        continue
                    else:    
                        i = 0
                        while i < 3:
                            if agency == data['agency']:
                                break
                            else:
                                i += 1
                                if i < 3 :
                                    print("Você possui apenas", 3-i, "tentativas")
                                    agency = int(input("Digite sua Agencia Novamente: (obs: 4 digitos) >> "))
                                    continue
                                else:
                                    self.block()
                        break
                return agency

            elif tp == 'password':
                while True:
                    try:
                        password = int(input("Digite sua Senha: (obs: 5 digitos) >> "))
                        while password < 10000 or password > 99999:
                                password = int(input("Apenas 5 Digitos \nDigite sua Senha: (obs: 5 digitos) >> "))
                    except ValueError:
                        print("Digite apenas numeros inteiros")
                        continue
                    else:
                        
                        
                        i = 0
                        while i < 3:
                            if password == data['password']:
                                break
                            else:
                                i += 1
                                if i < 3 :
                                    print("Você possui apenas", 3-i, "tentativas")
                                    password = int(input("Digite sua Senha Novamente: (obs: 5 digitos) >> "))
                                    continue
                                else:
                                    self.block()    
                            
                        break
                return password

            elif tp == 'code':
                while True:
                    try:
                        code = int(input("Digite seu Código de Segurança: (obs: 4 digitos) >> "))
                        while code < 1000 or code > 9999:
                                code = int(input("Apenas 4 Digitos \nDigite seu Código de Segurança: (obs: 4 digitos) >> "))
                    except ValueError:
                        print("Digite apenas numeros inteiros")
                        continue
                    else:   
                        i = 0
                        while i < 3:
                            if code == data['codeSecurity']:
                                break
                            else:
                                i += 1
                                if i < 3 :
                                    print("Você possui apenas", 3-i, "tentativas")
                                    code = int(input("Digite seu Código de Segurança Novamente: (obs: 4 digitos) >> "))
                                    continue
                                else:
                                    self.block()
                        break
                return code

        #--------- Acessa o Banco de Dados -----------
        data = open("data.txt", "r", encoding="UTF-8")
        i = 0
        txt = data.readlines()
        data.close()
        controlLine = 0 

        cpf = str(input("Digite seu CPF: "))

        #------ Pega os dados do banco de dados e formata para JSON --------
        for data in txt:
            auxCpf = ""
            auxIndex = 0
            for i in data:
                if i == '"':
                    continue
                if i != ":":
                    auxCpf  += i
                    auxIndex += 1
                else:
                    
                    auxIndex += 1
                    
                    break
            self.__dataComplete.append(json.loads("{"+data+"}")) #Salva toda a estrutura de dados
            self.__cpf.append(auxCpf) #Salva apenas o CPF
            self.__dataBank.append(json.loads(data[auxIndex+2:])) #Salva apenas os dados para operações
            
            
            if str(auxCpf) == cpf:
                #---------- Caso o CPF seja encontrado, inicia o processo de autenticação
                dataDict = json.loads(data[auxIndex+2:])
                self.__accountBank =  {
                "name": autentication(dataDict, 'name'),
                "account": autentication(dataDict, 'account'),
                "agency": autentication(dataDict, 'agency'),
                "password": autentication(dataDict, 'password'),
                "codeSecurity": autentication(dataDict, 'code') ,
                "balance": float(dataDict['balance']),
                }
                #----------- Se tudo for autenticado, o usuario será levado para sessão de operações -------
            else:
                #------- Caso não encontre o CPF no banco de dados, retorna uma mensagem e fecha o programa -----
                controlLine += 1
                if controlLine == len(txt):
                    print("CPF não encontrado em nosso banco de dados")
                    exit()  
                continue
    
    #---------------------------- OPERAÇÕES BANCARIA -------------------------------

    #------------- Função da Sessão de operações bancarias
    def operations(self):
        while True:
            os.system('cls') or None
            question = input("Qual operação que deseja fazer?\n 1- Saque\n 2- Deposito\n 3- Transferencia\n 4- Ver Saldo Bancario\n 5- Sair\n\n>> ").lower()
            if question == "1" or question == "saque":
                os.system('cls') or None
                self.withdraw()
                self.saving()
                os.system('cls') or None
                
            elif question == "deposito" or question == "2":
                os.system('cls') or None
                self.deposit()
                self.saving()
                os.system('cls') or None
                
            elif question == "transferencia" or question == "3":
                os.system('cls') or None
                self.tranferencia()
                self.saving()
                print("Valor Transferido com Sucesso!\n")    
                input("\nAperte ENTER para continuar >> ")
                os.system('cls') or None
                

            elif question == "ver saldo bancario" or question == "4":
                self.getBankBalance()
                os.system('cls') or None
            elif question == "sair" or question == "5":
                exit()
            else:
                pass
        return None
    #OPERAÇÃO PARA VER SALDO BANCARIO
    def getBankBalance(self):
        os.system('cls') or None
        print("Seu saldo bancario é de R$", self.__accountBank['balance'])
        input("\nAperte ENTER para continuar >> ")

    #OPERAÇÃO DE TRANSFERENCIA
    def tranferencia(self):

        #Sessão que verifica se conta bancaria digitada para onde o dinheiro vai ser transferido existe           
        while True:
            try:
                account = int(input("Digite a Conta Bancaria que deseja fazer transferencia >> "))
                verifyAc = self.verify(account, "account")
            except ValueError:
                print("Digite apenas numeros!")
                continue
            if account < 100000 and account > 999999:
                print("Digite apenas 6 numeros!")
                continue
            elif verifyAc[1]:
                print("Digite uma conta bancaria existente!")
                continue
            else:
                break
        while True:
            try:
                agency = int(input("Digite Agencia da Conta Bancaria >> "))
                verifyAg = self.verify(agency, "agency")
            except ValueError:
                print("Digite apenas numeros!")
                continue
            if agency < 1000 and agency > 9999:
                print("Digite apenas 4 numeros!")
                continue
            elif verifyAc[1]:
                print("Digite uma Agencia valida!")
                continue
            else:
                break
        while True:
            #---------------- Sessão de transferencia -------------------------------------------
            try:
                transfer = float(input("Digite a quantia que deseja transferir >> "))
            except ValueError:
                print("Digite apenas numeros!")
                continue
            if self.verify(transfer, "balance"):
                print("Sua Conta saldo insuficiente para fazer a transferencia\nTente Novamente\n!")
                continue
            else:
                #Sessão que gera a transferencia bancaria e modifica os saldos
                self.__accountBank['balance'] -= transfer
                for index in range(len(self.__dataBank)):
                    if self.__dataBank[index]['account'] == verifyAc[0] and self.__dataBank[index]['agency'] == verifyAg[0]:
                        self.__dataBank[index]['balance'] = float(self.__dataBank[index]['balance']) + transfer  
                        break
                break
        
    #OPERAÇÃO DE SAQUE
    def withdraw(self):
        while True:
            try:
                value = float(input("Deseja Sacar quantos R$?\n >> "))
            
            except ValueError:
                print("Digite apenas numeros!!!")
                continue
            else: 
                break
        if value >= self.__accountBank["balance"]:
            self.__accountBank["balance"] = 0
        else:
            self.__accountBank["balance"] -= value
        print("Valor Sacado com Sucesso!\n")
        input("\nAperte ENTER para continuar >> ")

    #OPERAÇÃO DE DEPOSITO
    def deposit(self):
        while True:
            try:
                value = float(input("Deseja Depositar quantos R$?\n >> "))
            except ValueError:
                print("Digite apenas numeros!!!")
                continue
            else: 
                break
        self.__accountBank["balance"] += value
        print("Valor Depositado com Sucesso!\n")
        input("\nAperte ENTER para continuar >> ")

    #VERIFICAÇÃO DE CONTAS BANCARIAS NO BANCO DE DADOS
    def verify(self, index, tp):
        #função responsavel por fazer verificações pontuais de dados no bancos de dados
        if tp == "balance":
            if index > self.__accountBank['balance']:
                return True
            else:
                return False
        auxVerify = 0
        for data in self.__dataBank:
            if tp == "name":
                if index == data['name']:
                    return [data['name'] ,False]
                else:
                    auxVerify += 1
                    if auxVerify == len(self.__dataBank):
                        return [1, True]
                    else:
                        continue

            elif tp == "account":
                if index == data['account']:
                    return [data['account'], False]
                else:
                    auxVerify += 1
                    if auxVerify == len(self.__dataBank):
                        return [1, True]
                    else:
                        continue

            elif tp == "agency":
                if index == data['agency']:
                    return [data['agency'],False]
                else:
                    auxVerify += 1
                    if auxVerify == len(self.__dataBank):
                        return [1, True]
                    else:
                        continue
            

    #FORMATA, SALVA E ATUALIZA O BANCO DE DADOS    
    def saving(self):
        for data in range(len(self.__dataBank)):
            if self.__dataBank[data]['name'] == self.__accountBank['name'] and  self.__dataBank[data]['account'] == self.__accountBank['account'] and self.__dataBank[data]['agency'] == self.__accountBank['agency'] and self.__dataBank[data]['codeSecurity'] == self.__accountBank['codeSecurity']:
                self.__dataBank[data] = self.__accountBank
        newData = open("data.txt", "w", encoding="UTF-8")
                   
        for data in self.__dataBank:
            for i in range(len(self.__dataComplete)):
                if data['name'] == self.__dataComplete[i][self.__cpf[i]]['name'] and  data['account'] == self.__dataComplete[i][self.__cpf[i]]['account'] and data['agency'] == self.__dataComplete[i][self.__cpf[i]]['agency'] and data['codeSecurity'] == self.__dataComplete[i][self.__cpf[i]]['codeSecurity']:
                    self.__dataComplete[i][self.__cpf[i]] = data
        for i in range(len(self.__dataComplete)):
            self.__dataString = json.dumps(self.__cpf[i])+ ":" + "{" + '"name"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['name']) + "," + '"account"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['account']) + "," + '"agency"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['agency']) + "," + '"password"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['password']) + "," + '"codeSecurity"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['codeSecurity']) + "," + '"balance"' + ":" + json.dumps(self.__dataComplete[i][self.__cpf[i]]['balance']) + "}"+"\n"
            newData.write(self.__dataString)
        newData.close()


    
    #METODOS ESTATICOS  
    
    @staticmethod
    def block():
        os.system('cls') or None
        print("SEU ACESSO FOI BLOQUEADO\nEncerrando o programa....")
        exit()
    
Bank(int(input("Olá, \n Digite 1 entrar em sua conta bancaria \n Digite 2 para criar conta \n>> ")))