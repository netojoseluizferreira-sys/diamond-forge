# models.py
# Define a classe Cofre com encapsulamento do saldo.
# O atributo __saldo é privado e só pode ser modificado
# pelos métodos depositar() e sacar(). Demonstra o princípio
# de encapsulamento da POO: proteção do estado interno.

class Cofre:
    def __init__(self):
        # Atributo privado: só acessível dentro da classe
        self.__saldo: float = 0.0

    # Depósito: aceita apenas valores positivos.
    # Se o valor for negativo, exibe mensagem de erro.
    def depoistar(self, valor: float) -> None:
        if valor < 0:
            print("Não é possivel depositar valores negativos")
        else:
            self.__saldo += valor

    # Saque: só realiza se houver saldo suficiente.
    # Retorna True se o saque foi feito, False caso contrário.
    def sacar(self, valor: float) -> bool:
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False

    # Retorna o saldo formatado em moeda brasileira.
    def ver_saldo(self) -> str:
        return f"Seu saldo é de: R${self.__saldo:,.2f}"