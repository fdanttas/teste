import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float



#atribuindo valores.
pessoa1 = Pessoa("Marta", 30 , 70.0, 1.65)


print("Dados da pessoa: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} anos, peso: {pessoa1.peso}kg , altura: {pessoa1.altura}m")


