# 💎 The Diamond Forge — 60 Exercícios de Python Avançado

> *"O C me deu o metal. O Twin Forge me deu a liga. O Diamond Forge me dará o brilho."*

**The Diamond Forge** é uma jornada de 60 exercícios de **Python Avançado**, projetada para transformar um programador que já domina a sintaxe em um **engenheiro de software que entende as profundezas da linguagem**. Não se trata de aprender a usar Python — trata-se de dominar os mecanismos internos que fazem do Python uma das linguagens mais poderosas do mundo.

---

## 🎯 Objetivo

Dominar os conceitos avançados de Python que separam um programador comum de um especialista:

- Orientação a Objetos avançada (metaclasses, descriptors, decoradores)
- Iteradores e geradores
- Tipagem estática com type hints
- Concorrência e assincronia
- Meta-programação e introspecção

---

## 🧱 Estrutura da Jornada

A jornada é dividida em **6 blocos**, cada um com 10 exercícios e um projeto integrador.

| Bloco | Tema | Foco Principal |
|:------|:-----|:---------------|
| **1** | POO Fundamentos | Classes, objetos, herança, encapsulamento, métodos mágicos, dataclasses |
| **2** | POO Avançado | Decoradores, propriedades, descritores, metaclasses, ABC, mixins |
| **3** | Iteráveis e Geradores | Iteradores customizados, `yield`, expressões geradoras, `itertools` |
| **4** | Tipagem Estática e Type Hints | `typing`, `Protocol`, `Generic`, `TypeVar`, `TypedDict`, `Literal`, `mypy` |
| **5** | Concorrência e Assincronia | `threading`, `multiprocessing`, `asyncio`, `async`/`await`, filas, futures |
| **6** | Meta-programação e Fechamento | Context managers, introspecção, `__init_subclass__`, `__setattr__`, AST básico |

---

## 🔄 Metodologia: Retroatividade e Exposição Precoce

### Retroatividade (Manutenção)
Nos blocos 2 a 6, **2 exercícios por bloco** revisam conceitos de blocos anteriores, aplicando-os em novos contextos. O conhecimento não é descartado — é **reutilizado e aprofundado**.

### Exposição Precoce (Ganchos)
Nos blocos 1 a 5, **1 exercício por bloco** introduz superficialmente um tópico do próximo bloco. O objetivo é ver o conceito antes de dominá-lo, criando conexões neurais que serão reforçadas depois.

### Progressão de Complexidade
Cada bloco começa com fixação (sintaxe direta), passa por fáceis (aplicação em cenários simples) e termina com médios e difíceis (combinação de conceitos).

---

## 🏗️ Projetos Integradores

Cada bloco culmina em um projeto que consolida o aprendizado:

| Projeto | Após o Bloco | O que consolida |
|:--------|:-------------|:----------------|
| **`biblioCLI`** | Bloco 1 | Classes, herança, dataclasses, persistência JSON |
| **`validatORM`** | Bloco 2 | Decoradores, descriptors, metaclasses, ABC |
| **`asyncLog`** | Bloco 3 | Geradores, `itertools`, `async`/`await`, `asyncio` |
| **`shopforge`** | Bloco 4 | Type hints, Protocol, Generic, mypy, API com FastAPI |
| **`mlforge`** | Bloco 5 | Concorrência, pipelines, MLOps simplificado |
| **`diamond-prediction`** | Bloco 6 | Projeto final integrador: predição com API, Docker e CI/CD |

---

## 📁 Estrutura de Diretórios


Diamond-Forge/
│
├── bloco1-fundamentos-poo/
│   ├── 001-a-boas-vindas/
│   │   ├── models.py
│   │   └── main.py
│   ├── 002-a-biblioteca/
│   │   └── main.py
│   ├── ...
│   └── projeto-biblioCLI/
│
├── bloco2-poo-avancado/
│   ├── ...
│   └── projeto-validatORM/
│
├── bloco3-iteraveis-geradores/
│   ├── ...
│   └── projeto-asyncLog/
│
├── bloco4-tipagem-estatica/
│   ├── ...
│   └── projeto-shopforge/
│
├── bloco5-concorrencia/
│   ├── ...
│   └── projeto-mlforge/
│
├── bloco6-metaprogramacao/
│   ├── ...
│   └── projeto-diamond-prediction/
│
├── README.md          ← você está aqui
├── CHANGELOG.md
└── PROGRESS.md


**Nota:** Cada exercício contém apenas os arquivos `.py` necessários. A documentação central vive no README principal — sem READMEs individuais por exercício.

---

## 🛡️ O Paredão Python (Code Runner)

Para manter o mesmo rigor do C Crucible, todo exercício é executado com:

```json
"python": "python -u -X dev -W error $fileName"
```

| Flag | O que faz |
|:------|:----------|
| `-u` | Modo unbuffered — saída imediata, sem buffer. |
| `-X dev` | Modo desenvolvedor — ativa verificações extras (warnings de depreciação, etc.). |
| `-W error` | **Transforma qualquer warning em erro.** O equivalente ao `-Werror` do C. |

---

## 📊 Progresso

| Bloco | Exercícios | Projeto | Status |
|:------|:----------|:--------|:-------|
| 1 — POO Fundamentos | 10/10 | `biblioCLI` | ✅ **Concluído** 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩 100% |
| 2 — POO Avançado | 0/10 | `validatORM` | 🔄 **Em Execução** 🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜ 0% |
| 3 — Iteráveis e Geradores | 0/10 | `asyncLog` | ⬛ Planejado |
| 4 — Tipagem Estática | 0/10 | `shopforge` | ⬛ Planejado |
| 5 — Concorrência | 0/10 | `mlforge` | ⬛ Planejado |
| 6 — Meta-programação | 0/10 | `diamond-prediction` | ⬛ Planejado |
| **Total** | **10/60** | | 🟩⬜⬜⬜⬜⬜ 17% |

---

## 🏗️ Projetos Integradores

Cada bloco culmina em um projeto que consolida o aprendizado:

| Projeto | Após o Bloco | O que consolida | Repositório |
|:--------|:-------------|:----------------|:------------|
| **`biblioCLI`** | Bloco 1 | Classes, herança, dataclasses, persistência JSON | [github.com/netojoseluizferreira-sys/biblioCLI](https://github.com/netojoseluizferreira-sys/biblioCLI) |
| **`validatORM`** | Bloco 2 | Decoradores, descriptors, metaclasses, ABC | (em breve) |
| **`asyncLog`** | Bloco 3 | Geradores, `itertools`, `async`/`await`, `asyncio` | (em breve) |
| **`shopforge`** | Bloco 4 | Type hints, Protocol, Generic, mypy, API com FastAPI | (em breve) |
| **`mlforge`** | Bloco 5 | Concorrência, pipelines, MLOps simplificado | (em breve) |
| **`diamond-prediction`** | Bloco 6 | Projeto final integrador: predição com API, Docker e CI/CD | (em breve) |

---

## 🧠 Regra de Ouro

O objetivo não é "saber Python". É olhar para um código e entender **o que está acontecendo por baixo dos panos** — como os objetos são criados, como os decoradores funcionam, como a memória é gerenciada, como a concorrência é orquestrada.

Quando isso se tornar automático, Python deixou de ser uma linguagem e virou uma **extensão do pensamento**.

---

**Forjado por Enkel (Neto) © 2026**
*"Do brilho da abstração ao domínio da meta-programação."*

