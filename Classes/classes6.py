import os
from dataclasses import dataclass
os.system("cls || clear")
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float
    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nIdade: {self.idade}, \nPeso: {self.peso}, \nAltura: {self.altura}\n\n")
lista_de_pessoas = []
QUANTIDADE_PESSOAS = 2

for i in range(QUANTIDADE_PESSOAS):
    pessoa = Pessoa(nome=input("Digite seu nome:"),
                    idade=int(input("Digite sua idade:")),
                    peso=float(input("Digite seu peso:")),
                    altura=float(input("Digite sua altura:")))
    lista_de_pessoas.append(pessoa)

nome_arquivo = "pessoas.txt"
with open(nome_arquivo, "w") as arquivo:
    for pessoa in lista_de_pessoas:
        arquivo.write(f"{pessoa.nome}, {pessoa.idade}, {pessoa.peso}, {pessoa.altura}\n")

print("\nExibindo dados: ")
for pessoa in lista_de_pessoas:    
    pessoa.exibir_dados()

