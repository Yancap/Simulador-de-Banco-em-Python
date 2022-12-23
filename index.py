from view import BankView
import os
print("------------ Bem-Vindo ao PyBank ------------\n")
print("   Digite 1 para Login\n   Digite 2 para Registrar\n")
quest = int(input(" >> "))

if quest == 1:
    BankView().loginIn()
    BankView().operationsMethod()
else:
    BankView().register()
    quest = input("\nDeseja Logar-se?\n 1 - Sim\n 2 - Nao\n>> ").lower()
    if quest == "sim" or quest == "1":
        BankView().loginIn()
        BankView().operationsMethod()
    else:
        os.system('cls') or None
        print("Obrigado, Volte Sempre!")
        input("Aperte ENTER para fechar o programa >> ")
        exit()