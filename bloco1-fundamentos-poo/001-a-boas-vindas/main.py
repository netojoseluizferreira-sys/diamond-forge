# main.py
# Ponto de entrada do programa.
# Importa a classe Pessoa do módulo models e demonstra seu uso.

from models import Pessoa

# Leitura da entrada com tratamento básico
nome = input("Nome: ").title()          # Capitaliza o nome
idade = int(input("Idade: ").strip())   # Converte para inteiro

# Criação de uma instância de Pessoa
p1 = Pessoa(nome, idade)

# Chamada do método cumprimentar() e impressão do retorno
print(p1.cumprimentar())