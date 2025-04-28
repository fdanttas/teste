import os

os.system("cls || clear")


import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Tente adivinhar o número que estou pensando (entre 1 e 100).")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))

        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print("Parabéns! Você acertou!")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
