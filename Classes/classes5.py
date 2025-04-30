import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int

def exibir_dados(self):
    print("\nExibindo dados: ")
    print(f"Nome: {self.nome}, \nIdade: {self.idade}\n\n")

lista_de_pacientes = []
QUANTIDADE_PACIENTES = 2

for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(nome=input("Digite seu nome:"))
                    idade=int(input("Digite sua idade:"))
    lista_de_pacientes.append(paciente)
    
print("\nExibindo dados: ")
for paciente in lista_de_pacientes:    
    paciente.exibir_dados()


