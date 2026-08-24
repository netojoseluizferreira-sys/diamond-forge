# 💎 The Diamond Forge — Makefile Global
# Comandos para executar exercícios e projetos com o Paredão Python

PYTHON = python3
FLAGS = -u -X dev -W error
FLAKE8 = flake8
MYPY = mypy

# Executa um arquivo específico com o Paredão
# Uso: make run ARGS="caminho/para/arquivo.py"
run:
	@if [ -z "$(ARGS)" ]; then \
		echo "Uso: make run ARGS=\"caminho/para/arquivo.py\""; \
	else \
		$(PYTHON) $(FLAGS) $(ARGS); \
	fi

# Verifica estilo com flake8
lint:
	@$(FLAKE8) . --exclude=.git,__pycache__ --max-line-length=88

# Verifica type hints com mypy
typecheck:
	@$(MYPY) . --ignore-missing-imports

# Executa tudo: lint + typecheck
check: lint typecheck

.PHONY: run lint typecheck check