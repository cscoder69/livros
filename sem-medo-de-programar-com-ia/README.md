# SEM MEDO de programar com IA

## Arquivos de código que acompanham o livro

Autor do livro: Claudio Santos. Materiais de estudo para os 22 capítulos do livro. Distribuição v3.3, de 16 de outubro de 2026.

Este pacote reúne exercícios, soluções de referência, testes, dados fictícios e roteiros de apoio. Para começar, extraia o ZIP inteiro. Mantenha juntas as pastas **`codigos`** e **`materiais`**: os caminhos indicados no livro partem desta pasta.

Não é preciso instalar Git para utilizar estes arquivos. Se você recebeu o ZIP diretamente do autor, extraia-o e localize esta pasta do livro. Se estiver lendo no GitHub, volte à página inicial do repositório, escolha **Code** e depois **Download ZIP**. Após extrair o download, abra a pasta **`sem-medo-de-programar-com-ia`**. O download do repositório pode incluir materiais de outros livros; as instruções desta página se referem somente a este livro.

## **[GITHUB]** Endereço dos materiais

A [pasta deste livro no GitHub](https://github.com/cscoder69/livros/tree/main/sem-medo-de-programar-com-ia) é a entrada para estes materiais. A [página inicial do repositório livros](https://github.com/cscoder69/livros) oferece o download em **Code → Download ZIP**. Depois de extrair, abra **`sem-medo-de-programar-com-ia`**; dentro dela estão as pastas **`codigos`** e **`materiais`**.

## Indicadores do livro e dos guias

Os rótulos abaixo aparecerão **em negrito**, junto das orientações correspondentes. Eles ajudam a reconhecer onde realizar a ação ou que tipo de referência está sendo apresentado:

| Indicador | O que significa | Próxima ação |
| --- | --- | --- |
| **[GITHUB]** | Acesso aos arquivos fornecidos pelo autor. | Consultar a pasta do livro ou baixar os materiais. |
| **[COLAB]** | Prática pelo navegador, no Google Colab. | Usar o arquivo `.ipynb` indicado e o procedimento do capítulo 4. |
| **[COMPUTADOR]** | Prática local, no seu computador. | Usar Python e a pasta ou o arquivo `.py` informado. |
| **[CONSULTA]** | Fonte externa para conferir ou aprofundar uma explicação. | Abrir o link quando precisar; a leitura pode continuar sem consultar todas as fontes. |
| **[GIT]** | Registro de versões com a ferramenta Git. | Seguir a orientação opcional do capítulo 8, com a preparação indicada ali. |

**GitHub e Git têm papéis diferentes.** O primeiro é o serviço em que você encontra os materiais do livro. O segundo registra versões dos arquivos de um projeto e será apresentado no capítulo 8. Baixar os exemplos pelo GitHub não exige instalar Git.

A marca **[CONSULTA]** identifica a fonte externa; a explicação que a acompanha continua fazendo parte da leitura.

O rótulo acompanha uma instrução ou uma referência; a simples menção a uma ferramenta numa explicação não exige repetir a marca. Quando um parágrafo apresentar alternativas, os rótulos indicarão os percursos correspondentes. A marca não significa que aquela ação já foi executada ou conferida nesta edição.

## **[COLAB]** Conhecer a opção pelo navegador

O **Google Colab** é um serviço do Google para abrir arquivos de código e executar Python pelo navegador. O processamento acontece no serviço; nesse percurso, você não precisa instalar Python no computador. Para seguir a opção apresentada no capítulo 4, usará uma conta Google e conexão com a internet.

Ele aparece como uma alternativa para a primeira prática porque permite reunir explicações, blocos de código e resultados na mesma página. Você executa um bloco e observa sua saída antes de passar ao seguinte. Os arquivos `.ipynb` fornecidos pelo autor foram organizados dessa forma. A escolha oferece esse modo de acompanhar os exemplos; não é uma exigência para aprender o método do livro.

Cada ferramenta tem uma função no percurso:

| Ferramenta | Para que será usada |
| --- | --- |
| **GitHub** | Encontrar e baixar os arquivos fornecidos pelo autor. |
| **Google Colab** | Abrir sua cópia de um arquivo `.ipynb` e executar seus blocos de código. |
| **Ferramenta de IA escolhida por você** | Conversar sobre o código, pedir explicações e propor alterações. |

O arquivo vem do GitHub. Você o envia ao Colab e trabalha em sua própria cópia; não há um projeto do autor publicado nesse serviço para procurar. A conversa com a IA acontece separadamente. O organizador resultante executa em Python: cadastrar uma tarefa não faz uma consulta à IA.

### Como essa opção será mencionada ao longo do livro

Quando uma prática disser **“no navegador”** ou pedir para abrir um arquivo **`.ipynb`**, estará retomando esse percurso pelo Colab. O capítulo indicará o arquivo, e o capítulo 4 ensinará o envio e a ordem de execução das células. Os guias **`README.md`** das pastas também apresentam a opção correspondente.

Quando disser **“no computador”** ou **“execução local”**, usará os arquivos **`.py`** com Python instalado. Você pode escolher esse caminho desde a primeira prática; a preparação está no guia **`PREPARAR-PYTHON.md`**. Algumas práticas posteriores, como a separação em módulos e o laboratório MCP, têm instruções locais próprias.

**[CONSULTA]** **Estado da conferência desta edição:** o Colab documenta o envio de arquivos existentes, mas a abertura e a execução dos arquivos deste livro na interface do serviço ainda não foram verificadas. As conferências registradas foram locais; executar as células localmente não substitui o teste no serviço. [Fonte: documentação do Colab](https://research.google.com/colaboratory/faq.html).

## Por onde começar

1. Leia o capítulo 4 do livro e abra a pasta **`codigos/capitulo-04`**. Os nomes numerados de pastas e arquivos acompanham os capítulos do livro.
2. Escolha **`exercicio.ipynb`** para a opção pelo navegador ou **`inicial.py`** para o computador. Deixe as soluções **`referencia.ipynb`** e **`solucao.py`** para comparar depois da tentativa.
3. **[COLAB]** Para executar pelo navegador, acesse o [Google Colab](https://colab.research.google.com/), entre com sua conta Google e use a opção de enviar um arquivo do computador. Selecione **`exercicio.ipynb`**.
4. No navegador, leia as instruções e execute as células, os pequenos blocos de código, de cima para baixo; após uma alteração, execute novamente a célula e a demonstração. No computador, siga o guia de preparação abaixo e execute `python inicial.py` na pasta da sua cópia de estudo. Salve o trabalho antes de repetir a execução.

Os arquivos terminados em **`.ipynb`** reúnem instruções e blocos de código para executar dessa forma. Os terminados em **`.py`** são programas Python para execução no computador. O formato do arquivo não indica uma função de IA: o organizador funciona sem consultar um modelo. Sua conversa com a ferramenta de IA acontece separadamente.

Para instalar Python e abrir o terminal na pasta correta, consulte [Preparar Python](PREPARAR-PYTHON.md). Se preferir executar no computador, leia também o **`README.md`** da pasta escolhida: é o guia de instruções daquele conjunto. Os primeiros exemplos não exigem bibliotecas externas. A prática de integração do capítulo 19 tem dependências próprias e instruções específicas.

## Localizar cada prática

Consulte o [guia por capítulo](GUIA-POR-CAPITULO.md). Alguns capítulos propõem leitura, planejamento ou registro, sem um novo programa separado. As versões iniciais, os casos com defeito preparado e as soluções têm finalidades diferentes.

| Pasta | Conteúdo |
| --- | --- |
| [Primeira prática](codigos/capitulo-04/README.md) | Cadastro de tarefas e recusa de títulos inválidos; capítulo 4. |
| [Comparação de propostas](codigos/capitulo-05/README.md) | Duas propostas para avaliar; capítulo 5. |
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

Os materiais têm conferências locais registradas durante a preparação do livro. Na versão 4.0, depois da renomeação, todos os programas, testes e os nove arquivos `.ipynb` foram executados de novo localmente, conforme **`VERSAO.json`**. A preparação da distribuição confere a integridade e a correspondência dos arquivos; não representa nova execução de todas as práticas. A abertura e a execução na interface hospedada do Colab não foram verificadas nesta edição.

A licença de uso desta distribuição ainda não foi definida pelo autor. Consulte as informações de versão antes de redistribuir ou incorporar os materiais a outro projeto. A ausência de uma licença não é uma autorização adicional de uso.

## Histórico de atualização

Consulte [o histórico dos materiais](ATUALIZACOES.md) para identificar o que mudou nesta distribuição. A versão 4.0 renomeou pastas e arquivos para acompanhar a numeração dos capítulos; quem baixou uma versão anterior deve baixar o conjunto novamente.
