# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e o projeto segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [0.2.0] — 2026-10-05
### Adicionado
- Projeto integrador do Bloco 1: `biblioCLI`
  - Sistema de gerenciamento de biblioteca via linha de comando
  - 3 classes de domínio: `Livro`, `Prateleira`, `Biblioteca`
  - Persistência JSON com escrita atômica (tmp + replace)
  - CLI interativo com comandos: add, rm, list, shelves, search, help, exit
  - Suíte completa de testes: 95 testes, 99% de cobertura
  - Repositório: https://github.com/netojoseluizferreira-sys/biblioCLI

### Alterado
- README atualizado com status do Bloco 1 (concluído) e do Bloco 2 (em execução)
- PROGRESS atualizado com o registro do Bloco 1 completo

### Aprendido
- `defaultdict(list)` acelera muito quando a estrutura interna é dict de listas
- `@dataclass` só vale quando a classe é puramente dados (no biblioCLI, não fez sentido)
- Escrita atômica em JSON é obrigatória para persistência não corromper
- Testes com `pytest` e `--cov` dão visibilidade real da cobertura

---

## [0.1.0] — 2026-08-23
### Adicionado
- 10 exercícios do Bloco 1 — POO Fundamentos
  - Classes, objetos, herança, encapsulamento
  - Métodos mágicos (`__str__`, `__repr__`, `__eq__`)
  - Métodos de classe (`@classmethod`) e estáticos (`@staticmethod`)
  - Properties (`@property`, `@setter`)
  - Gancho: `@property` no exercício 010 preparando decoradores do Bloco 2
- Estrutura inicial do repositório
  - README, CHANGELOG, PROGRESS
  - Paredão Python configurado (`-u -X dev -W error`)

---