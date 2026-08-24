# main.py
# Demonstra o uso do contador de instâncias da classe Ourives.
# Três objetos são criados, e o total é consultado via @classmethod.

from models import Ourives

# Cria três instâncias (cada uma incrementa _total em 1)
o1 = Ourives()
o2 = Ourives()
o3 = Ourives()

# Consulta o total de ourives criados usando o método de classe
print(Ourives.Quantos())