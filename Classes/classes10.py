import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereço: str
    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nData de Admissão: {self.data_de_admissao}, \nMatrícula: {self.matricula}, \nEndereço: {self.endereço}\n\n")
lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 3

for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(nome=input("Digite seu nome:"),
                              data_de_admissao=input("Digite sua data de admissão:"),
                              matricula=input("Digite sua matrícula:"),
                              endereço=input("Digite seu endereço:"))
    lista_de_funcionarios.append(funcionario)
nome_arquivo = "funcionarios.txt"
with open(nome_arquivo, "w") as arquivo:
    for funcionario in lista_de_funcionarios:
        arquivo.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereço}\n")
print("\nDados salvos com sucesso!\n")


@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereço: str

    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nData de Nascimento: {self.data_de_nascimento}, \nEndereço: {self.endereço}\n\n")
lista_de_clientes = []
QUANTIDADE_CLIENTES = 3
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(nome=input("Digite seu nome:"),
                      data_de_nascimento=input("Digite sua data de nascimento:"),
                      endereço=input("Digite seu endereço:"))
    lista_de_clientes.append(cliente)
nome_arquivo = "clientes.txt"
with open(nome_arquivo, "w") as arquivo:
    for cliente in lista_de_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.data_de_nascimento}, {cliente.endereço}\n")
print("\nDados salvos com sucesso!\n")