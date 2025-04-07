import os 

os.system("cls || clear")

def par_ou_impar(numero):
    if numero % 2 ==0 :
        print("Numero par. ")
    else: 
        print("Numero impar. ")

print("= PAR OU IMPAR =")
numero = int(input("Digite um numero: "))
par_ou_impar(numero)