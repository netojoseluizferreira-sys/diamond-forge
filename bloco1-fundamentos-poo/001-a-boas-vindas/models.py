# models.py
# Define a classe Pessoa, que representa o núcleo do cadastro.
# Demonstra os fundamentos de POO: atributos de instância, construtor
# (__init__), type hints e um método de instância comum.

class Pessoa:
    # Construtor: recebe nome e idade e os armazena como atributos
    # da instância. Os type hints documentam os tipos esperados.
    def __init__(self, nome: str, idade: int):
        self.nome = nome    # Atributo de instância (str)
        self.idade = idade  # Atributo de instância (int)

    # Método de instância: retorna uma apresentação formatada.
    # Acessa os atributos da instância via self.
    def cumprimentar(self) -> str:
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."