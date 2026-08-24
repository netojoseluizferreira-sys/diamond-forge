# 🛡️ O Paredão Python — Dicionário de Flags

## Comando Padrão

Todo exercício do Diamond Forge é executado com:

```bash
python -u -X dev -W error nome_do_arquivo.py
```

## Glossário

| Flag | O que faz | Equivalente no C |
|:-----|:----------|:-----------------|
| `-u` | Modo unbuffered — a saída é escrita imediatamente. | `setbuf(stdout, NULL)` |
| `-X dev` | Modo desenvolvedor — ativa verificações extras. | `-Wall -Wextra` |
| `-W error` | Transforma warnings em erros. | `-Werror` |
| `-O` | Modo otimizado — remove `assert` e `__debug__`. | `-O2` (parcialmente) |

## Linters (Verificação Estática Manual)

```bash
flake8 nome_do_arquivo.py
```

Verifica:
- Erros de sintaxe
- Estilo (PEP 8)
- Complexidade ciclomática
- Importações não usadas
- Variáveis não usadas

```bash
mypy nome_do_arquivo.py
```

Verifica:
- Type hints corretos
- Compatibilidade de tipos
- Retornos de função

## Regra de Ouro

Warning é erro. Código sujo não passa. O ourives não aceita nada menos que a excelência.

---
Documentação mantida como parte do regime de qualidade do Diamond Forge.