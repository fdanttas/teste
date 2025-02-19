import os

os.system("clear") # Limpa o terminal

primeira_nota = float(input("Digite sua primeira nota:"))
segunda_nota = float(input("Digite sua primeira nota:"))
terceira_nota = float(input("Digite sua primeira nota:"))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")    





