# SEM MEDO de programar com IA

## Arquivos de código que acompanham o livro

Autor do livro: Claudio Santos. Materiais de estudo para os 22 capítulos do livro. Distribuição v3.1, de 15 de outubro de 2026.

Este pacote reúne exercícios, soluções de referência, testes, dados fictícios e roteiros de apoio. Para começar, extraia o ZIP inteiro. Mantenha juntas as pastas **`codigos`** e **`materiais`**: os caminhos indicados no livro partem desta pasta.

Não é preciso instalar Git para utilizar estes arquivos. Se você recebeu o ZIP diretamente do autor, extraia-o e localize esta pasta do livro. Se estiver lendo no GitHub, volte à página inicial do repositório, escolha **Code** e depois **Download ZIP**. Após extrair o download, abra a pasta **`sem-medo-de-programar-com-ia`**. O download do repositório pode incluir materiais de outros livros; as instruções desta página se referem somente a este livro.

## Endereço dos materiais

A [pasta deste livro no GitHub](https://github.com/cscoder69/livros/tree/main/sem-medo-de-programar-com-ia) é a entrada para estes materiais. A [página inicial do repositório livros](https://github.com/cscoder69/livros) oferece o download em **Code → Download ZIP**. Depois de extrair, abra **`sem-medo-de-programar-com-ia`**; dentro dela estão as pastas **`codigos`** e **`materiais`**.

## Por onde começar

1. Leia o capítulo 4 do livro e abra a pasta **`codigos/capitulo-02`**. A pasta conserva uma numeração anterior; ela corresponde ao capítulo 4 atual.
2. Comece por **`exercicio.ipynb`**, o arquivo de código inicial fornecido pelo autor. Deixe **`referencia.ipynb`** para comparar depois da tentativa.
3. Para executar pelo navegador, acesse o [Google Colab](https://colab.research.google.com/), entre com sua conta Google e use a opção de enviar um arquivo do computador. Selecione **`exercicio.ipynb`**.
4. Leia as instruções e execute as células, os pequenos blocos de código, de cima para baixo. Depois de modificar uma função, execute novamente sua célula e a demonstração. Salve ou baixe sua cópia modificada.

Os arquivos terminados em **`.ipynb`** reúnem instruções e blocos de código para executar dessa forma. Os terminados em **`.py`** são programas Python para execução no computador. O formato do arquivo não indica uma função de IA: o organizador funciona sem consultar um modelo. Sua conversa com a ferramenta de IA acontece separadamente.

Se preferir executar no computador, leia o **`README.md`** da pasta escolhida: é o guia de instruções daquele conjunto. Os primeiros exemplos não exigem bibliotecas externas. A prática de integração do capítulo 19 tem dependências próprias e instruções específicas.

## Localizar cada prática

Consulte o [guia por capítulo](GUIA-POR-CAPITULO.md). Alguns capítulos propõem leitura, planejamento ou registro, sem um novo programa separado. As versões iniciais, os casos com defeito preparado e as soluções têm finalidades diferentes.

| Pasta | Conteúdo |
| --- | --- |
| [Primeira prática](codigos/capitulo-02/README.md) | Cadastro de tarefas e recusa de títulos inválidos; capítulo 4. |
| [Comparação de propostas](codigos/capitulo-03/README.md) | Duas propostas para avaliar; capítulo 5. |
| [Organizador](codigos/organizador/README.md) | Prioridades, filtros, prazos, testes, importação, recorrência e referência final. |
| [Projeto existente](codigos/projeto-existente/README.md) | Fila de atendimento com defeito preparado para investigação; capítulo 16. |
| [Laboratório de agente](codigos/laboratorio-agente/README.md) | Cópias de início e resultado, diferenças e registro de integridade; capítulo 17. |
| [Integração MCP](codigos/integracao-mcp/README.md) | Cliente e servidor locais para comunicação entre programas; capítulo 19. |
| **`materiais`** | Fichas de tarefa, contexto, retomada, integração, automação, leitura e desafio final. |

## Como usar as versões

Faça suas alterações em uma cópia de estudo. Não misture arquivos de etapas diferentes: algumas funções têm o mesmo nome, mas correspondem a pontos distintos do percurso. Use o guia por capítulo para escolher a base.

Os dados dos exemplos são fictícios. O organizador mantém as tarefas em memória; fechar ou reiniciar a execução descarta esses dados. Exportar para texto JSON não equivale a gravar um arquivo automaticamente. Os guias de cada grupo explicam os limites restantes.

**`erro_atraso.py`** e a fila inicial contêm defeitos intencionais. No laboratório de agente, os documentos internos das cópias históricas foram preservados: use primeiro o guia principal do laboratório para distinguir o estado inicial do corrigido.

## Versão e conferências

[VERSAO.json](VERSAO.json) identifica esta distribuição. [MANIFESTO-SHA256.json](MANIFESTO-SHA256.json) relaciona os arquivos e seus resumos de integridade, chamados hashes; eles ajudam a verificar se um arquivo corresponde a esta distribuição. O manifesto não contém seu próprio hash.

Os materiais têm conferências locais registradas durante a preparação do livro. A montagem deste ZIP confere integridade, sintaxe e correspondência dos arquivos; não representa uma nova execução de todas as práticas. A abertura e a execução na interface hospedada do Colab ainda precisam ser conferidas antes da publicação definitiva.

A licença de uso desta distribuição ainda não foi definida pelo autor. Consulte as informações de versão antes de redistribuir ou incorporar os materiais a outro projeto. A ausência de uma licença não é uma autorização adicional de uso.

## Histórico de atualização

Consulte [o histórico dos materiais](ATUALIZACOES.md) para identificar o que mudou nesta distribuição. Os nomes de pastas usados no livro são preservados nas atualizações.
