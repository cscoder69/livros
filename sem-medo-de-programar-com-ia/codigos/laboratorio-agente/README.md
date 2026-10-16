# Laboratório de agente — registro de uma execução real

Caso didático preparado e executado pelo Codex na sessão de autoria de 14/10/2026. O assistente conhecia o defeito preparado; não é avaliação cega nem comparação de produtos. A tarefa local foi reproduzir a consulta, acrescentar um teste que revele o defeito e proteja contra seu retorno, corrigir a condição e conferir alterações.

As pastas inicio e resultado são cópias independentes. Abra um terminal em inicio para a base de quatro testes e em resultado para seis testes após a correção:

```text
python -m unittest -v test_fila.py
python -m fila.cli --prioridade alta
```

Use este guia para localizar as duas cópias. Os arquivos `README.md` e `CONTRATO.md` dentro de `inicio` e `resultado` vieram da base e foram preservados como parte do registro histórico. Suas frases sobre quatro testes e defeito preparado descrevem o início; não descrevem o resultado corrigido. A referência relativa a `../laboratorio-agente/resultado` nesses documentos também veio da base: a partir da pasta deste guia, o caminho correto é simplesmente `resultado`.

A cópia `inicio` devolve A1/A2/A3 e tem quatro métodos de teste; `resultado` devolve apenas A1 e tem seis métodos. O teste novo falhou antes da correção e passou depois. `alteracao.diff` registra as diferenças; a execução detalhada está no relatório editorial da etapa 09, separado dos arquivos necessários ao exercício. O organizador original não foi alterado. Somente `fila/consultas.py` e `test_fila.py` diferem entre as duas cópias históricas.

Para repetir com outro agente, forneça CONTRATO.md, indique esta cópia e permita alteração apenas desses dois arquivos. Peça leitura da base, resultado anterior, teste que falha antes de corrigir, nova execução e comparação. Um pedido delimita o trabalho; isolamento técnico exige configuração do ambiente escolhido. Não presuma que as permissões de um produto são iguais às desta sessão.
