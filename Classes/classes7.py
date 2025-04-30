import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass

class Livro:
    nome: str
    autor: str
    categoria:str
    preco: int

    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nAutor: {self.autor}, \nCategoria: {self.categoria}, \nPreço: {self.preco}\n\n")

lista_de_livros = []
QUANTIDADE_LIVROS = 3
for i in range(QUANTIDADE_LIVROS):
    livro = Livro(nome=input("Digite o nome do livro:"),
                  autor=input("Digite o autor do livro:"),
                  categoria=input("Digite a categoria do livro:"),
                  preco=int(input("Digite o preço do livro:")))
    lista_de_livros.append(livro)

    nome_arquivo ="catalogos_livros.txt"
    with open(nome_arquivo, "w") as arquivo:
        for livro in lista_de_livros:
            arquivo.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n")
print("\nDados salvos com sucesso!\n")
print("\nExibindo dados: ")
for livro in lista_de_livros:    
    livro.exibir_dados()



