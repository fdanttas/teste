import os

os.system("Clear")

primeiro_numero = int(input("Digite seu primeiro numero: "))
segundo_numero=int(input("Digite seu segundo numero: "))

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero

print("\nExibindo resultados: ")
print(f"Primeiro numero:{primeiro_numero}")
print(f"Segundo numero: {segundo_numero}")
print(f"Menor: {menor}")                                   
print(f"Maior: {maior}")




