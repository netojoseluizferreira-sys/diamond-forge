# models.py
# Define a hierarquia Funcionario -> Gerente.
# Funcionario tem salário base e método salario_total().
# Gerente herda de Funcionario, adiciona bônus percentual e
# sobrescreve salario_total() para calcular salário com bônus.

class Funcionario:
    def __init__(self, nome: str, salario: float) -> None:
        self._nome = nome                    # atributo protegido
        self._salario_base = salario         # atributo protegido

    # Retorna o salário base (sem bônus)
    def salario_total(self) -> float:
        return self._salario_base

    # Representação amigável do funcionário
    def __str__(self) -> str:
        return f"Funcionario: {self._nome}; Salario: R${self.salario_total():.2f}"


class Gerente(Funcionario):
    def __init__(self, nome: str, salario: float, bonus_percentual: float) -> None:
        # Chama o construtor da classe base para inicializar nome e salário
        super().__init__(nome, salario)
        self.bonus_percentual = bonus_percentual   # bônus específico do gerente

    # Sobrescreve salario_total() para incluir o bônus
    def salario_total(self) -> float:
        # Obtém o salário base usando o método da classe base
        salario_base = super().salario_total()
        # Aplica o bônus: salário = base * (1 + bônus)
        return salario_base * (1 + self.bonus_percentual)

    # Herda __str__ da classe base, que já chama salario_total()