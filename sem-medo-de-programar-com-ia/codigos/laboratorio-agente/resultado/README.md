# Projeto existente — fila de atendimento

Base de estudo preparada, com defeito intencional. Não é uma aplicação de cliente real. Python 3.12, biblioteca padrão. Abra um terminal nesta pasta.

```text
python -m unittest -v test_fila.py
python -m fila.cli
python -m fila.cli --prioridade alta
```

A suíte inicial tem quatro métodos e passa. A consulta por alta, porém, viola o contrato. Antes de alterar, leia CONTRATO.md e acompanhe CLI, serviço, consulta, dados e apresentação. Compare códigos selecionados, não só quantidade. O resultado corrigido está em ../laboratorio-agente/resultado. Abra essa pasta separadamente para não misturar módulos fila de versões diferentes. Não altere os dados para fazer a demonstração passar.
