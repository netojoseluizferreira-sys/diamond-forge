# Projeto: biblioCLI

Projeto integrador do **Bloco 1 — POO Fundamentos**.

## Sobre

Sistema de gerenciamento de biblioteca via linha de comando. Aplica os
conceitos de POO, dataclasses e persistência JSON consolidados no
primeiro bloco do Diamond Forge.

O projeto gerencia livros organizados por gênero em prateleiras, com
persistência em disco e uma suíte completa de testes.

## Conceitos aplicados

- Classes e objetos
- Composição e delegação
- Encapsulamento com `@property`
- Métodos mágicos (`__str__`, `__repr__`, `__eq__`, `__hash__`)
- Persistência em JSON com escrita atômica
- Testes automatizados com `pytest`

## Funcionalidades

- Cadastrar livros com título, autor, ano e gênero
- Organizar livros automaticamente em prateleiras por gênero
- Listar livros (todos ou por gênero)
- Buscar por título, autor, ano, gênero ou id
- Remover exemplares por título (com quantidade opcional)
- Persistência automática: carrega ao iniciar, salva após cada operação

## Testes

Suíte com 95 testes automatizados e **99% de cobertura**.

Verificação com:

```bash
pytest --cov --cov-report=term-missing
```

## Repositório

🔗 [github.com/netojoseluizferreira-sys/biblioCLI](https://github.com/netojoseluizferreira-sys/biblioCLI)

## Status

✅ **v1.0 — Completo e testado**


---

## 5. Comando para criar o arquivo

```powershell
cd "C:\Users\Usuário\Desktop\projetos-integradores\Diamond-Forge"

# Cria a pasta e o README
New-Item -ItemType Directory -Force -Path "bloco1-fundamentos-poo\projeto-biblioCLI" | Out-Null
New-Item -ItemType File -Force -Path "bloco1-fundamentos-poo\projeto-biblioCLI\README.md" | Out-Null
```