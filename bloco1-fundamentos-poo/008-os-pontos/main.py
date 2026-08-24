# main.py
# Ponto de entrada: lê dois pares de coordenadas, cria dois objetos
# Pontos e compara-os com ==.

from models import Pontos

# Lê e cria o primeiro ponto
coord1 = Pontos(
    float(input("X1 = ")),
    float(input("Y1 = "))
)

# Lê e cria o segundo ponto
coord2 = Pontos(
    float(input("X2 = ")),
    float(input("Y2 = "))
)

# Compara os dois pontos usando __eq__
print("Iguais" if coord1 == coord2 else "Diferentes")