# main.py
# Ponto de entrada: lê dois números e uma operação, e usa os
# métodos estáticos da classe Calculadora para calcular o resultado.

from models import Calculadora

while True:
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    op = input("Operação (X para sair): ")

    match op:
        case '+':
            print(f"{Calculadora.somar(n1, n2):.2f}")
        case '-':
            print(f"{Calculadora.subtrair(n1, n2):.2f}")
        case '*':
            print(f"{Calculadora.multiplicar(n1, n2):.2f}")
        case '/':
            if n2 != 0:
                print(f"{Calculadora.dividir(n1, n2):.2f}")
            else:
                print("Erro, divisão por 0")
        case _ if op in "xX":
            print("Saindo...")
            break