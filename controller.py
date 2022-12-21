from model import BankData
from dal import BankDal
class BankController:
    #Fazer as operações de registro e cadastro e a view
    def __init__(self, operation):
        if operation == "register":
            pass
        elif operation == "login":
            pass

    class Validation:
        def __init__(self):
            self.dataArray = BankDal.loadData()
            

        def validationCpf(self, cpf: str):
            if len(cpf) != 11:
                return "invalid"
            for index in self.dataArray[0]:
                if cpf == index:
                    return "exist"
            return "nonexistent"

        def validationName(self, name: str):
            for index in self.dataArray[1]:
                if name.lower() == index['name']:
                    return "exist"
            return "nonexistent"
        @staticmethod
        def validationPassword(password):
            if len(str(password)) != 5:
                return "invalid"
            

        def validationAccount(self, account: int):
            if len(str(account)) != 6:
                return "invalid"
            for index in self.dataArray[1]:
                if account == index['account']:
                    return "exist"
            return "nonexistent"

        def validationAgency(self, agency: int):
            if len(str(agency)) != 4:
                return "invalid"
            for index in self.dataArray[1]:
                if agency == index["agency"]:
                    return "exist"
            return "nonexistent"

        def validationCode(self, code: int):
            if len(str(code)) != 4:
                return "invalid"
            for index in self.dataArray[1]:
                if code == index["codeSecurity"]:
                    return "exist"
            return "nonexistent"

    class Operations:
        def __init__(self, accountPeople: BankData):
            self.accountPeople = accountPeople
        def withdraw(self, value):
            if self.accountPeople.balance == 0:
                return
            self.accountPeople.balance -= value
            BankDal.saveData(self.accountPeople)

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
            
        def getBankBalance():
            return self.accountPeople.balance   
valida = BankController.Validation()
BankController.Operations(BankData("11122233344", "barack", 54321, 129799, 1847, 9620, 1120.0)).transfer(valida, 253035, 1000)