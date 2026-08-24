# models.py
# Define a hierarquia Animal -> Cachorro.
# Animal tem nome e som, e o método falar().
# Cachorro herda de Animal e define o som padrão "au au".

class Animal:
    def __init__(self, nome: str, som: str):
        self.nome = nome
        self.som = som

    # Retorna a representação do som do animal
    def falar(self) -> str:
        return f"{self.nome} faz {self.som}"


class Cachorro(Animal):
    # Construtor da subclasse: recebe apenas o nome.
    # O som "au au" é passado para a classe base via super().
    def __init__(self, nome: str, som: str = "au au"):
        super().__init__(nome, som)