from model import BankData
from dal import BankDal
import random
import json

class BankController:
    #Fazer as operações de registro e cadastro e a view
    

    class Validation:
        def __init__(self):
            self.dataArray = BankDal.loadData()
            self.attempts = 0

        def returnData(self, cpf):
            self.dataArray = BankDal.loadData()
            for data in self.dataArray[2]:
                if cpf in data:
                    return json.loads("{"+data+"}")

        def create(self, tipo):

            if tipo == "agency":
                randomNum = random.randint(1000,9999)
                while self.validationAgency(randomNum) == "exist":
                    randomNum = random.randint(1000,9999)
                return randomNum

            elif tipo == "account":
                randomNum = random.randint(100000,999999)
                while self.validationAccount(randomNum) == "exist":
                    randomNum = random.randint(100000,999999)
                return randomNum

            elif tipo == "code":
                randomNum = random.randint(1000,9999)
                while self.validationCode(randomNum) == "exist":
                    randomNum = random.randint(1000,9999)
                return randomNum

        def validationCpf(self, cpf: str):
            if len(cpf) != 11:
                return "invalid"
            for index in self.dataArray[0]:
                if cpf == index:
                    return "exist"
            return "notexist"

        def validationName(self, name: str, tp = "register", data = "none"):
            if tp == "register":
                for index in self.dataArray[1]:
                    if name.lower() == index['name']:
                        return "exist"
                return "notexist"
            else:
                
                if name.lower() == data['name']:
                    return "exist"
                return "notexist"

        def validationPassword(self, password, tp = "register", data = "none"):
            if len(str(password)) != 5:
                return "invalid"
            if tp == "entrace":
                
                if password == data['password']:
                    return "exist"
                return "notexist"
            
        def validationAccount(self, account: int, tp = "register", data = "none"):
            if len(str(account)) != 6:
                return "invalid"
            if tp == "register":
                for index in self.dataArray[1]:
                    if account == index['account']:
                        return "exist"
                return "notexist"
            else:
                
                if account == data['account']:
                    return "exist"
                return "notexist"

        def validationAgency(self, agency: int, tp = "register", data = "none"):
            if len(str(agency)) != 4:
                return "invalid"
            if tp == "register":
                for index in self.dataArray[1]:
                    if agency == index["agency"]:
                        return "exist"
                return "notexist"
            else:
                
                if agency == data["agency"]:
                    return "exist"
                return "notexist"

        def validationCode(self, code: int, tp = "register", data = "none"):
            if len(str(code)) != 4:
                return "invalid"
            if tp == "register":
                for index in self.dataArray[1]:
                    if code == index["codeSecurity"]:
                        return "exist"
                return "notexist"
            else:
                if code == data["codeSecurity"]:
                    return "exist"
                return "notexist"

        def autentication(self, condition):
            if self.attempts <= 3:
                if condition == "exist":
                    return "exist"
                elif condition == "notexist":
                    self.attempts += 1
                    return "notexist"
                elif condition == "invalid":
                    return "invalid"
                pass
            else:
                print("SEU ACESSO FOI BLOQUEADO!")
                input("Aperte ENTER para sair >> ")
                exit()
    class Operations:
        def __init__(self, accountPeople: BankData):
            self.accountPeople = accountPeople
        def withdraw(self, value):
            if value > self.accountPeople.balance:
                return 'invalid'
            self.accountPeople.balance -= value
            BankDal.saveData(self.accountPeople)
            return 'valid'
        def deposit(self, value):
            self.accountPeople.balance += value
            BankDal.saveData(self.accountPeople)

        def transfer(self, object, account, value):
            if self.accountPeople.balance == 0: 
                return "invalid"
            self.accountPeople.balance -= value
            index = 0
            
            for data in object.dataArray[1]:
                if data["account"] == account:
                    data["balance"] += value
                    break
                index += 1
            BankDal.saveData(self.accountPeople)
            BankDal.saveData(BankData(object.dataArray[0][index],object.dataArray[1][index]["name"],object.dataArray[1][index]["password"], object.dataArray[1][index]["account"],object.dataArray[1][index]["agency"],object.dataArray[1][index]["codeSecurity"],object.dataArray[1][index]["balance"]))
            
        def getBankBalance(self):
            return self.accountPeople.balance   

