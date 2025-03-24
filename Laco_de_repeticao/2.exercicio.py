import os

os.system("cls || clear")

soma = 0

while True:
 print("""
 -------------- MENU ----------------      
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$ 25,00
2 \t Lasanha \t\t R$ 20,00    
3 \t Strogonoff \t\t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00

""")
 opção = int(input("Digite o numero da opçao desejada: "))

match opcao:
    case 1:
        prato = "Picanha"
        preco = 25
    case 2:
        prato = "Lasanha"
        preco = 20
    case 3:
        prato = "Strogonof"
        preco = 18
    case 4:
        prato = "Bife acebolado"
        preco = 15
    case 5:
        prato = "Pão com ovo"
        preco = 0

soma += preco
continuar = input("Deseja escolher outro prato? \nDigite 'S' ou 'N': ").lower()
if continuar == "n" :
    break
os.system("cls || clear")
    


print(f"\nTotal a pagar: R$ {soma}")
    