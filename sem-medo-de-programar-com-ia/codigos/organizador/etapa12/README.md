# Etapa 12 — Refatoração sem recursos posteriores

Esta cópia contém os comportamentos da etapa08, separados em `dominio.py` e `apresentacao.py`. Não inclui importação nem recorrência.

Na pasta `etapa12`, com Python instalado:

```text
python -m unittest -v test_etapa12.py
```

Os oito testes importam os arquivos desta pasta. Não execute a comparação reutilizando um interpretador que já tenha carregado outro módulo chamado `dominio`; use um processo novo, como no comando acima.

Compare com `../etapa08.py` para identificar o deslocamento da função de listagem. Os contratos de entrada e saída permanecem iguais.
