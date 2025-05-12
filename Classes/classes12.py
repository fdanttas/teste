import os
import time
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_de_nascimento: str
    cpf: str
    funcao: str
    def exibir_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, \nData de Nascimento: {self.data_de_nascimento}, \nCPF: {self.cpf}, \nFunção: {self.funcao}\n\n")
lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 2
for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(nome=input("Digite seu nome: "),
                              data_de_nascimento=input("Digite sua data de nascimento:"),
                              cpf=input("Digite seu CPF:"),
                              funcao=input("Digite sua função:"))
    
    def verificar_lista_vazia(lista_funcionarios):
        if not lista_funcionarios:
            print("\nA lista está vazia.")
            return True
        return False

    def adicionar_funcionario(lista_funcionarios):
        nome = input("Digite o nome que deseja adicionar: ")
        lista_funcionarios.append(nome)
        print(f"\n{nome} adicionado com sucesso.")
    def mostrar_funcionarios(lista_funcionarios):
        # Vefificar se a lista está vazia.
        if verificar_lista_vazia(lista_funcionarios):
            return
        print("\n - Lista de funcionários - ")
        for funcionario in lista_funcionarios:
            print(f"- {funcionario}")
    def atualizar_funcionario(lista_funcionarios):
        # Verificar se a lista está vazia.
        if verificar_lista_vazia(lista_funcionarios):
            return
        mostrar_funcionarios(lista_funcionarios)
        funcionario_antigo = input("Digite o nome que deseja atualizar: ")
        if funcionario_antigo in lista_funcionarios:
            novo_funcionario = input(f"Digite o novo nome para {funcionario_antigo}: ")
            indice = lista_funcionarios.index(funcionario_antigo)
            lista_funcionarios[indice] = novo_funcionario
            print(f"{funcionario_antigo} foi atualizado para {novo_funcionario}.")
        else:
            print(f"\nO nome {funcionario_antigo} não foi encontrado.")
    def excluir_funcionario(lista_funcionarios):
        # Verificar se a lista está vazia.
        if verificar_lista_vazia(lista_funcionarios):
            return
        # Mostra lista de usuários
        mostrar_funcionarios(lista_funcionarios)
        funcionario_remover = input("Digite o nome que deseja remover: ")
        if funcionario_remover in lista_funcionarios:
            lista_funcionarios.remove(funcionario_remover)
            print(f"{funcionario_remover} foi removido com sucesso.")
        else:
            print(f"\nO nome {funcionario_remover} não foi encontrado.")


nome = []
 
while True:
        print("\n - Menu - ")
        print("1. Adicionar funcionário")
        print("2. Mostrar funcionários")
        print("3. Atualizar funcionário")
        print("4. Excluir funcionário")
        print("5. Sair")
    
        opcao = input("Escolha uma opção: ")
    
        if opcao == "1":
            adicionar_funcionario(lista_de_funcionarios)
        elif opcao == "2":
            mostrar_funcionarios(lista_de_funcionarios)
        elif opcao == "3":
            atualizar_funcionario(lista_de_funcionarios)
        elif opcao == "4":
            excluir_funcionario(lista_de_funcionarios)
        elif opcao == "5":
            print("\nSaindo...")
            time.sleep(1)
            break
        else:
            print("\nOpção inválida.")


