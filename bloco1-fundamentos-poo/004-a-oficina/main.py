# main.py
# Ponto de entrada: demonstra polimorfismo com Carro e Moto.
# O mesmo método ligar() se comporta de forma diferente
# dependendo da classe do objeto.

from models import Moto, Carro

# Criação das instâncias
motocycle = Moto()
car = Carro()

# Loop do menu
while True:
    print("C - CARRO\nM - MOTO")
    veiculo = input("Veiculo: ").strip().upper()[0]

    match veiculo:
        case 'C':
            print(car.ligar())       # chama o ligar() de Carro
        case 'M':
            print(motocycle.ligar()) # chama o ligar() de Moto
        case _:
            print("Veículo inexistente.")