import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: str



#atribuindo valores.
pessoa1 = Pessoa("Filipe","filipedantas@gmail.com"  , 71989537044, "Rua das flores, 212")


print("Exibindo resultados ")
print(f"Nome: {pessoa1.nome}, E-mail: {pessoa1.email}, Telefone: {pessoa1.telefone}, Endereço: {pessoa1.endereco}")


