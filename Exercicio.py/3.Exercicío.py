import os

os.system("clear")

primeiro_numero =float(input("Digite um numero:"))
segundo_numero = float(input("Digite seu segundo numero:"))


media = (primeiro_numero + segundo_numero) /2 
produto = primeiro_numero * segundo_numero
soma = primeiro_numero + segundo_numero

if primeiro_numero < segundo_numero:
    menor =primeiro_numero
    maior= segundo_numero
else:
    menor= segundo_numero
    maior= primeiro_numero

print("\nExibindo resultados: ")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Soma: {soma}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")