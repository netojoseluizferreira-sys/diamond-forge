# models.py
# Define a classe Circulo com propriedades (@property).
# O raio é encapsulado com getter e setter, e área/perímetro
# são calculados sob demanda. Demonstra o uso de @property
# para validação e encapsulamento de atributos.

from math import pi

class Circulo:
    def __init__(self, raio: float):
        # Usa o setter da propriedade para validar o raio inicial
        self.raio = raio

    # Getter da propriedade raio
    @property
    def raio(self) -> float:
        return self.__raio

    # Setter da propriedade raio: valida se o valor é positivo
    @raio.setter
    def raio(self, novo_raio: float) -> None:
        if novo_raio <= 0:
            raise ValueError("Raio inválido, valor negativo.")
        else:
            self.__raio = novo_raio

    @property
    def area(self) -> float:
        return self.__raio ** 2 * pi

    @property
    def perimetro(self) -> float:
        return self.__raio * 2 * pi