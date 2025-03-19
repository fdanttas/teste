# Leitura dos dados
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

# Se sexo for "F" e estado civil for "CASADA", solicita o tempo de casada
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Há quantos anos você é casada? "))
else:
    tempo_casada = None

# Exibe os dados do usuário
print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

# Se a pessoa for casada, exibe o tempo de casada
if tempo_casada is not None:
    print(f"Tempo de casada: {tempo_casada} anos")
