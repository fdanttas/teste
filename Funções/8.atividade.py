import os

os.system("cls || clear")

def calcular_media(nota1, nota2) :
    soma = 0
    soma = nota1 + nota2
    resultado = soma / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        print("Aprovado .")
    else:
        print("Reprovado .")

print("= Notas =")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = calcular_media(nota1,nota2)
verificar_resultado(media)