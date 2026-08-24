# main.py
# Ponto de entrada: cria um Cachorro e exibe seu som.

from models import Cachorro

# Criação do cachorro (o som "au au" é definido por padrão na subclasse)
dog = Cachorro(input("Nome: ").title())

# Exibe o som do cachorro
print(dog.falar())