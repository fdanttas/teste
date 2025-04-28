import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa():
    nome: str
    email: str
    telefone: int
    endereco: str

def exibindo_dados(self):
    print("\nExibindo dados: ")
    print(f"Nome: {self.nome}, E-mail: {self.email}, Telefone: {self.telefone}, Endereço: {self.endereco}")

print("Solicitando dados ")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone: ") 
endereco = input("Digite seu endereço: ")

#atribuindo valores.
pessoa1 = Pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()   