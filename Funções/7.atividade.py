import os

os.system("cls || clear")

def positivo_negativo(numero):
    if numero < 0 :
        print("Numero negativo . ")

    elif numero == 0:
        print("0 é um número neutro")

    else: 
        print("Numero positivo . ")


print("= Positivo ou Negativo =")
numero = int(input("Digite um numero: "))
positivo_negativo(numero)