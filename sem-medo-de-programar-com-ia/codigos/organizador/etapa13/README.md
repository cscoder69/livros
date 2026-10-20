# Etapa 13 — Importação integral, sem recorrência

Esta cópia acrescenta leitura e escrita de texto JSON à versão refatorada. Não abre nem grava arquivos por conta própria. `intervalo_dias` e `proxima_gerada` ainda são campos desconhecidos nesta etapa.

Na pasta `etapa13`, com Python instalado:

```text
python -m unittest -v test_importacao.py
```

O esperado é a aprovação de três testes. Para usar no navegador, abra `../capitulo-13.ipynb`, que reúne as definições e demonstrações em células independentes dos arquivos locais.

Os registros externos exigem título textual válido e conclusão booleana. A validação adicional de tipo do título foi introduzida nesta fronteira de importação; não faz parte de uma mudança silenciosa na refatoração da etapa12.
