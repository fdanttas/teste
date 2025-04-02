import os

def logo_senai():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

def somar(n1, n2) :
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar (n1, n2):
    return n1 * n2

def dividir (n1, n2):
    return n1 / n2

logo_senai()
n1= int(input("Digite o primeiro número: "))

logo_senai()
n2= int(input("Digite o segundo número: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2) 
multiplicacao = multiplicar(n1, n2) 
divisao = dividir(n1, n2) 


logo_senai()
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisao: {divisao}")
