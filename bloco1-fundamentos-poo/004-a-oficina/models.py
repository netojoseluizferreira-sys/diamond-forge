# models.py
# Define a hierarquia de veículos com herança e sobrescrita de métodos.
# Veiculo é a classe base com o método ligar().
# Carro e Moto herdam de Veiculo e sobrescrevem ligar() com
# comportamentos específicos (polimorfismo).

class Veiculo:
    # Método base: retorna uma mensagem genérica de veículo ligado.
    def ligar(self) -> str:
        return "Veiculo ligado."

class Carro(Veiculo):
    # Sobrescreve ligar() com comportamento específico de carro.
    def ligar(self) -> str:
        return "Carro ligado: Vrum!"

class Moto(Veiculo):
    # Sobrescreve ligar() com comportamento específico de moto.
    def ligar(self) -> str:
        return "Moto ligada: Ram!"