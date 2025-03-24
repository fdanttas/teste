import os

os.system("cls || clear")

contador = 0
soma = 0

while True:
    nota = float(input("Digite uma nota: "))
    resposta = input("Deseja inserir mais uma nota? \nDigite 'S'ou 'N'" ).upper()
    if resposta == "N":
        break
    else:
        contador += 1
        soma += nota

if contador == 0:
    soma = nota
    contador = 1

media = soma / contador

print(f"\nMédia: {media}")