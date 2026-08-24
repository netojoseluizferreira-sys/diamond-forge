# main.py
# Ponto de entrada: cria um círculo, tenta alterar o raio e
# exibe área e perímetro.

from models import Circulo

# Criação do círculo com raio inicial
circle = Circulo(float(input("Raio: ")))

# Tentativa de alterar o raio (pode lançar ValueError se for inválido)
try:
    circle.raio = float(input("Novo Raio: "))
    print(f"{circle.area:.2f} {circle.perimetro:.2f}")
except ValueError as e:
    print(e)