# Exemplos do capítulo 4

Requer Python 3. Não usa bibliotecas externas, arquivos de dados ou chave de API.

- `exercicio.ipynb`: arquivo de código inicial para abrir no Google Colab e modificar.
- `referencia.ipynb`: arquivo de código com a solução e verificações automáticas.
- `inicial.py`: programa inicial, que aceita títulos inválidos de propósito.
- `solucao.py`: solução de referência.
- `verificar.py`: conferência automática da solução.

## Pelo navegador

Abra [Google Colab](https://colab.research.google.com/), entre com sua conta Google e procure no menu Arquivo (File) a opção para enviar um arquivo do computador. Selecione `exercicio.ipynb`. Execute as células de cima para baixo pelo botão de execução ao lado de cada bloco de código. Os nomes dos menus podem variar conforme o idioma e a versão do serviço.

Depois de editar a função, execute novamente sua célula e as células seguintes. A célula de demonstração começa com uma lista nova para evitar acúmulo de tarefas. Salve ou baixe sua cópia modificada; os dados da lista ficam apenas na memória da sessão.

## No computador, se já tiver Python

Na pasta destes exemplos:

```text
python inicial.py
python solucao.py
python verificar.py
```

## Resultado da demonstração corrigida

```text
Tarefa cadastrada.
Informe um título com pelo menos um caractere que não seja espaço.
Informe um título com pelo menos um caractere que não seja espaço.
0: [ ] Comprar pão
Tarefa concluída.
0: [x] Comprar pão
```

## Escopo e verificação editorial

Os títulos fornecidos às funções são textos; tratar valores de outros tipos está fora deste exercício. `strip()` também reconhece tabulações e quebras de linha como espaçamento. Títulos válidos são guardados como recebidos, sem remover seus espaços.

O teste de índice trata números inteiros fora da lista; não implementamos validação geral de tipos. As tarefas não persistem após encerrar a execução.

Os arquivos Python e as células dos arquivos de código foram verificados localmente com Python 3.12. A importação e a execução na interface hospedada do Colab ainda precisam de conferência antes da publicação. Site e repositório público ainda não foram publicados.
