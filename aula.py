import os
import time

os.system("cls || clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 0

while True:
    print(""" 
    
CODIGO | DESCRIÇÂO 
   1   | Adicionar pessoa
   2   | Exibir resultados
   3   | Sair            
""" )

    opcao = int(input("Digite sua opçao: "))

    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            sexo = input("Informe seu sexo - Use 'M' ou 'F': ").upper()
            salario = float(input("Digite seu salario : "))
            contador += 1
            soma_salario += salario
            maior_idade = max(maior_idade ,idade )
            menor_idade = min(menor_idade,idade)
            if sexo == "f" and salario >= 5000:
                mulheres5k += 1
            os.system("cls || clear")
        case 2:
            if contador > 0:
                media_salarial = soma_salario / contador
                print("\n= Exibindo resultados = ")
                print(f"Média salarial do grupo: {media_salarial}")
                print(f"Maior idade do grupo : {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salario a partir de 5k: {mulheres5k}") 
            else:
                print("\nNão foram informados os dados necessarios.")
            time.sleep(3)
            os.system("cls || clear")
        case 3:
            print("\n= FIM =")
            break
        case _:
            print("\nOpção inválida.")
            time.sleep(3)
            os.system ("cls || clear")    
        
    

