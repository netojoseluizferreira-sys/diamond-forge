# main.py
# Simula um caixa eletrônico simples com as operações de depósito,
# saque e consulta de saldo. Demonstra o uso da classe Cofre.

from models import Cofre
import os

# Função para limpar a tela do terminal (portável entre Windows e Unix)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criação do cofre (saldo inicial 0.0)
porquinho = Cofre()

# Loop principal do menu
while True:
    print("X - SAIR\nD - DEPOSITO\nS - SACAR")
    digito = input("Digite a ação que quer realizar: ").upper()[0]

    match (digito):
        case 'X':
            print("Fechando Cofre...")
            break

        case 'D':
            deposito = float(input("Digite o valor que quer depositar: ").strip())
            porquinho.depoistar(deposito)         # realiza o depósito
            print(porquinho.ver_saldo())          # mostra saldo atualizado

        case 'S':
            saque = float(input("Digite o valor que quer sacar: ").strip())
            saque_realizado = porquinho.sacar(saque)  # tenta sacar
            if saque_realizado:
                print(porquinho.ver_saldo())      # saldo atualizado
            else:
                print("Saldo insuficiente")       # falha no saque

        case _:
            print("Opção inválida, tente novamente")

    # Pausa para o usuário ver o resultado antes de limpar a tela
    input("Aperte ENTER para continuar...")
    limpar_tela()