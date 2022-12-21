from model import BankData
import json

class BankDal:
    @classmethod
    def createData(cls, dataBank: BankData):
        data = open("data.txt", "a", encoding="UTF-8")
        saveData = json.dumps(dataBank.cpf)+ ":" + "{" + '"name"' + ":" + json.dumps(dataBank.name).lower() + "," + '"account"' + ":" + json.dumps(dataBank.account) + "," + '"agency"' + ":" + json.dumps(dataBank.agency) + "," + '"password"' + ":" + json.dumps(dataBank.password) + "," + '"codeSecurity"' + ":" + json.dumps(dataBank.codeSecurity) + "," + '"balance"' + ":" + json.dumps(dataBank.balance) + "}"+"\n"
        data.write(saveData)
        data.close()
        

    @classmethod
    def readData(cls, cpf, name, password, account, agency, codeSecurity):
        return BankData(cpf, name, password, account, agency, codeSecurity)

    @classmethod
    def loadData(cls):
        auxData = open("data.txt", "r", encoding="UTF-8")
        dataX = auxData.readlines()
        auxData.close()
        dataCpf = []
        dataMain = []
        dataComplete = []
        for data in dataX:
            
            dataComplete.append(data) 
            for i in json.loads("{"+data+"}").values():
                dataMain.append(i)
            dataCpf += json.loads("{"+data+"}").keys()
        return [dataCpf, dataMain, dataComplete]

    @classmethod
    def saveData(cls, accountPeople: BankData):
        saveData = json.dumps(accountPeople.cpf)+ ":" + "{" + '"name"' + ":" + json.dumps(accountPeople.name).lower() + "," + '"account"' + ":" + json.dumps(accountPeople.account) + "," + '"agency"' + ":" + json.dumps(accountPeople.agency) + "," + '"password"' + ":" + json.dumps(accountPeople.password) + "," + '"codeSecurity"' + ":" + json.dumps(accountPeople.codeSecurity) + "," + '"balance"' + ":" + json.dumps(accountPeople.balance) + "}"+"\n"
        dataArray = BankDal.loadData()
        auxI = 0

        newData = open("data.txt", "w", encoding="UTF-8")
        for index in range(len(dataArray[0])):
            if dataArray[0][index] == accountPeople.cpf:
                dataArray[2][index] = saveData
        for data in dataArray[2]:
            newData.writelines(data)
        newData.close

