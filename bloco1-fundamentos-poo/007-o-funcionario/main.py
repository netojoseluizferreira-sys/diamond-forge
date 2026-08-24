# main.py
# Ponto de entrada: demonstra o uso de Funcionario e Gerente.
# Cria um funcionário normal e um gerente, e imprime seus dados.

from models import Gerente, Funcionario

# Criação de um funcionário comum
func = Funcionario(
    input("Nome: ").title(),
    float(input("Salario: ").strip())
)
print(func)

# Criação de um gerente (com bônus percentual)
staff = Gerente(
    input("Nome: ").title(),
    float(input("Salario: ").strip()),
    float(input("Bônus: "))
)
print(staff)