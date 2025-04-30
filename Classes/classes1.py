import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass 
class Pet:
    nome: str
    idade: int
    raca: str

#atribuindo valores.
pessoa1 = Pessoa("Marta", 30)
pessoa2 = Pessoa("Jose", 40)

pet1 = Pet("Toto", 4, "Pastor-alemão")
pet2= Pet("Hulk", 6 , "Pitbull")

print("Dados das pessoas: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}")

print("\nDados dos pets: ")
print(f"Nome: {pet1.nome}, idade: {pet1.idade}, raça: {pet1.raca}")
print(f"Raça: {pet2.raca}, idade: {pet2.idade}")