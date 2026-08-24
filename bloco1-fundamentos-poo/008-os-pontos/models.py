# models.py
# Define a classe Pontos com o método mágico __eq__.
# __eq__ permite comparar dois objetos com o operador ==,
# definindo o critério de igualdade: mesmos x e y.

class Pontos:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Define quando dois objetos Pontos são iguais.
    # O parâmetro 'outro' é o objeto do lado direito do ==.
    # A verificação isinstance evita comparação com tipos incompatíveis.
    def __eq__(self, outro):
        if not isinstance(outro, Pontos):
            return False
        return self.x == outro.x and self.y == outro.y