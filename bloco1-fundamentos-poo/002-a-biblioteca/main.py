# main.py
# Ponto de entrada: lê os dados de um livro, cria uma instância de Livro
# e demonstra a diferença entre str() e repr().

from models import Livro

# Leitura dos dados com formatação básica
titulo = input("Livro: ").title()    # Capitaliza o título
autor = input("Autor: ").title()     # Capitaliza o nome do autor
ano = int(input("Ano: ").strip())    # Converte ano para inteiro

# Criação da instância
book = Livro(titulo, autor, ano)

# print() usa __str__ internamente
print(book)

# repr() usa __repr__ internamente
print(repr(book))