import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Usuario:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str
    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nData de Nascimento: {self.data_nascimento}, \nRG: {self.rg}, \nCPF: {self.cpf}\n\n")
lista_de_usuarios = []
QUANTIDADE_USUARIOS = 5
for i in range(QUANTIDADE_USUARIOS):
    usuario = Usuario(nome=input("Digite seu nome:"),
                      data_nascimento=input("Digite sua data de nascimento:"),
                      rg=input("Digite seu RG:"),
                      cpf=input("Digite seu CPF:"))
    lista_de_usuarios.append(usuario)
nome_arquivo = "funcionarios.txt"
with open(nome_arquivo, "w") as arquivo:
    for usuario in lista_de_usuarios:
        arquivo.write(f"{usuario.nome}, {usuario.data_nascimento}, {usuario.rg}, {usuario.cpf}\n")
print("\nDados salvos com sucesso!\n")