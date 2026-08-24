# models.py
# Define a classe Ourives com um contador de instâncias usando
# atributo de classe e @classmethod.
# O atributo _total é compartilhado entre todas as instâncias,
# e o método Quantos() retorna quantos ourives já foram criados.

class Ourives:
    # Atributo de classe: pertence à classe, não às instâncias.
    # Começa em 0 e é incrementado a cada novo objeto.
    _total = 0

    # Construtor: incrementa o contador global da classe.
    # Usa Ourives._total explicitamente para acessar o atributo de classe.
    def __init__(self):
        Ourives._total += 1

    # Método de classe: recebe cls em vez de self.
    # Retorna o valor atual do contador de instâncias.
    @classmethod
    def Quantos(cls):
        return cls._total