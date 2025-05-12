import os
import time
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Aluno:
    nome: str
    data_de_nascimento: str
    ra: str
    curso: str
    endereço: str
    def self_exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nData de Nascimento: {self.data_de_nascimento}, \nRA: {self.ra}, \nCurso: {self.curso}, \nEndereço: {self.endereço}\n\n")
        
lista_de_alunos = []
QUANTIDADE_ALUNOS = 2
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(nome=input("Digite seu nome: "),
                  data_de_nascimento=input("Digite sua data de nascimento:"),
                  ra=input("Digite seu RA:"),
                  curso=input("Digite seu curso:"),
                  endereço=input("Digite seu endereço:"))
    lista_de_alunos.append(aluno)
    print("\nAluno adicionado com sucesso.")    
    time.sleep(1)
    os.system("cls || clear")

def verificar_lista_vazia(lista_alunos):
    if not lista_alunos:
        print("\nA lista está vazia.")
        return True
    return False
def adicionar_aluno(lista_alunos):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_alunos.append(nome)
    print(f"\n{nome} adicionado com sucesso.")
def mostrar_alunos(lista_alunos):
    # Vefificar se a lista está vazia.
    if verificar_lista_vazia(lista_alunos):
        return
    print("\n - Lista de alunos - ")
    for aluno in lista_alunos:
        print(f"- {aluno}")
def atualizar_aluno(lista_alunos):
    # Verificar se a lista está vazia.
    if verificar_lista_vazia(lista_alunos):
        return
    mostrar_alunos(lista_alunos)
    aluno_antigo = input("Digite o nome que deseja atualizar: ")
    if aluno_antigo in lista_alunos:
        novo_aluno = input(f"Digite o novo nome para {aluno_antigo}: ")
        indice = lista_alunos.index(aluno_antigo)
        lista_alunos[indice] = novo_aluno
        print(f"{aluno_antigo} foi atualizado para {novo_aluno}.")
    else:
        print(f"\nO nome {aluno_antigo} não foi encontrado.")
def excluir_aluno(lista_alunos):
    # Verificar se a lista está vazia.
    if verificar_lista_vazia(lista_alunos):
        return
    # Mostra lista de usuários
    mostrar_alunos(lista_alunos)
    aluno_remover = input("Digite o nome que deseja remover: ")
    if aluno_remover in lista_alunos:
        lista_alunos.remove(aluno_remover)
        print(f"\n{aluno_remover} removido com sucesso.")
    else:
        print(f"\nO nome {aluno_remover} não foi encontrado.")
def menu():
    print("1 - Adicionar Aluno")
    print("2 - Mostrar Alunos")
    print("3 - Atualizar Aluno")
    print("4 - Excluir Aluno")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao
# Criando lista de alunos.
alunos = []
# Mostrando menu.
while True:
    opcao = menu()
    match opcao:
        case 1:
            adicionar_aluno(lista_de_alunos)
        case 2:
            mostrar_alunos(lista_de_alunos)
        case 3:
            atualizar_aluno(lista_de_alunos)
        case 4:
            excluir_aluno(lista_de_alunos)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    if opcao != 1:
        time.sleep(5)
    os.system("cls || clear")

        
