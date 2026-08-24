# models.py
# Define a classe Calculadora com métodos estáticos.
# Métodos estáticos não acessam self nem cls — são funções comuns
# agrupadas em uma classe por organização lógica.
# Todos os métodos são @staticmethod, conforme o exercício.

class Calculadora:
    # Soma de dois números
    @staticmethod
    def somar(a, b):
        return a + b

    # Subtração de dois números
    @staticmethod
    def subtrair(a, b):
        return a - b

    # Multiplicação de dois números
    @staticmethod
    def multiplicar(a, b):
        return a * b

    # Divisão de dois números (não trata divisão por zero aqui;
    # a validação é feita na main)
    @staticmethod
    def dividir(a, b):
        return a / b