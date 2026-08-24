## 📄 `PROJECT.md`


# 📋 Projetos Integradores — Diamond Forge

Cada bloco do Diamond Forge culmina em um **projeto integrador** que consolida
os conceitos aprendidos. Estes projetos não são exercícios — são **mini-sistemas**
que demonstram domínio prático e servem como peças de portfólio.

---

## Projeto 1: `biblioCLI` (Após Bloco 1 — POO Fundamentos)

### Visão
Um CRUD de linha de comando para gerenciar uma biblioteca pessoal. O objetivo é
demonstrar domínio dos fundamentos de POO em um contexto real, sem frameworks.

### Requisitos
- Classes `Livro` e `LivroDigital` (herança)
- Classe `Biblioteca` que gerencia a coleção (composição)
- Dataclasses para os modelos
- Persistência em JSON (usando `json` nativo ou `pickle`)
- Interface CLI interativa

### Arquitetura

main.py      → loop principal e menus
models.py    → classes de domínio (Livro, LivroDigital, Biblioteca)
database.py  → leitura/escrita em JSON


### Decisões de Design
- **Herança**: `LivroDigital` herda de `Livro` e adiciona `formato` (PDF, EPUB).
- **Persistência**: JSON legível (em vez de pickle) para que o arquivo possa ser
  inspecionado manualmente.
- **Validação**: `__post_init__` do dataclass valida ano > 0.

### Critérios de Conclusão
- [ ] Criar, listar, buscar, atualizar e deletar livros.
- [ ] Salvar e carregar de arquivo JSON.
- [ ] Código tipado e documentado.
- [ ] Nenhum warning no Paredão (`-W error`).

---

## Projeto 2: `validatORM` (Após Bloco 2 — POO Avançado)

### Visão
Um mini framework de validação de dados usando descriptors e decoradores.
O objetivo é mostrar que validação não precisa ser repetitiva — pode ser
**declarativa**.

### Requisitos
- Descriptors para validar tipos e restrições
- Decoradores para validação de entrada/saída
- Classes de modelo com validação automática
- CRUD simples de usuários

### Arquitetura

main.py       → demonstração do framework
validators.py → descriptors (Positive, NonEmpty, MaxLength)
models.py     → classes que usam os validators


### Decisões de Design
- **Descriptors**: encapsulam a lógica de validação no atributo, não no método.
- **Composição**: os validators são reutilizáveis em qualquer classe.
- **Sem metaclasses ainda**: o Bloco 3 introduzirá metaclasses; aqui o foco
  é em descriptors e decoradores.

### Critérios de Conclusão
- [ ] Validators de tipo, positividade, tamanho máximo.
- [ ] Cada validação falha com mensagem clara.
- [ ] CRUD de usuários com validação automática.

---

## Projeto 3: `asyncLog` (Após Bloco 3 — Iteráveis e Geradores)

### Visão
Um sistema de logging assíncrono que grava mensagens em arquivo sem bloquear
a execução do programa. O objetivo é dominar geradores e `asyncio`.

### Requisitos
- Gerador que produz mensagens de log
- Corrotinas que consomem e gravam as mensagens
- Uso de `asyncio.Queue` para comunicação
- Simulação de múltiplos produtores

### Arquitetura

main.py    → orquestração das corrotinas
logger.py  → classes e funções de logging


### Decisões de Design
- **Geradores**: produzem mensagens sob demanda, sem carregar tudo em memória.
- **Asyncio**: a escrita em arquivo é simulada como operação assíncrona.
- **Desacoplamento**: produtores e consumidores comunicam-se via fila.

### Critérios de Conclusão
- [ ] Múltiplas corrotinas produzindo e consumindo logs.
- [ ] Escrita em arquivo não bloqueia o restante.
- [ ] Código com type hints básicos.

---

## Projeto 4: `shopforge` (Após Bloco 4 — Tipagem Estática)

### Visão
Um backend de e-commerce com FastAPI, totalmente tipado e testado. O objetivo
é aplicar type hints em uma API real, demonstrando que tipagem estática previne
bugs antes mesmo de executar.

### Requisitos
- Endpoints REST para produtos, carrinho e pedidos
- Modelos com Pydantic e `TypedDict`
- Type hints em todas as funções
- `mypy` rodando sem erros

### Arquitetura

main.py   → inicialização do FastAPI
api.py    → rotas e handlers
models.py → modelos de dados tipados
db.py     → persistência em SQLite (ou memória)

### Decisões de Design
- **Pydantic**: validação de entrada/saída com type hints.
- **SQLite**: banco simples, sem ORM pesado, para focar na tipagem.
- **Protocol**: contratos para dependências (ex: `Repositorio`).

### Critérios de Conclusão
- [ ] API com CRUD de produtos.
- [ ] `mypy` sem erros.
- [ ] Testes com pytest (opcional, mas desejável).

---

## Projeto 5: `mlforge` (Após Bloco 5 — Concorrência)

### Visão
Uma plataforma de MLOps simplificada: treinar, versionar, avaliar e implantar
modelos de machine learning. O objetivo é dominar concorrência e pipelines.

### Requisitos
- Pipelines de treinamento e avaliação
- Execução paralela de múltiplos modelos
- Uso de `ThreadPoolExecutor` ou `asyncio`
- Versionamento simples (salvar/carregar com `joblib`)

### Arquitetura

main.py     → CLI da plataforma
pipeline.py → classes de pipeline
train.py    → treinamento paralelo
models.py   → definição dos modelos


### Decisões de Design
- **Threads**: para I/O-bound (carregar dados).
- **Processos**: para CPU-bound (treinar modelos).
- **Futures**: para orquestrar execução paralela.

### Critérios de Conclusão
- [ ] Treinar 3+ modelos em paralelo.
- [ ] Comparar métricas e escolher o melhor.
- [ ] Salvar e carregar modelo escolhido.

---

## Projeto 6: `diamond-prediction` (Após Bloco 6 — Meta-programação)

### Visão
O projeto final: um sistema completo de predição de preços de diamantes
(ou outro dataset), com API, Docker, testes e CI/CD. É a obra-prima do
Diamond Forge.

### Requisitos
- Pipeline de ML completo (coleta, limpeza, treino, avaliação)
- API REST para predição (FastAPI)
- Containerização (Docker)
- Testes automatizados (pytest)
- Documentação (Sphinx ou docstrings)
- CI/CD (GitHub Actions)

### Arquitetura

app/                 → API
  ├── main.py
  ├── model.py       → carregamento do modelo
  └── schemas.py     → Pydantic models
pipeline/            → scripts de treinamento
tests/               → pytest
Dockerfile
docker-compose.yml
.github/workflows/   → CI/CD

### Decisões de Design
- **Context managers**: para gerenciar recursos (arquivos, conexões).
- **`__init_subclass__`**: para registrar automaticamente novos modelos.
- **AST/introspecção**: para validação de código em tempo de execução.

### Critérios de Conclusão
- [ ] API rodando em Docker.
- [ ] Testes passando com pytest.
- [ ] CI/CD rodando a cada push.
- [ ] Documentação completa.

---

**Forjado por Enkel (Neto) © 2026**
*"Cada projeto é uma joia. Juntas, formam a coroa."*