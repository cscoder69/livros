# **[COMPUTADOR]** Preparar Python para os exercícios

Este guia acompanha a primeira prática do capítulo 4 e descreve a preparação para executar os arquivos `.py` no computador.

Para estes exercícios, você não precisa compilar manualmente o código nem baixar um compilador separado: usará o **interpretador Python**. As conferências do organizador foram feitas com Python 3.12. A integração avançada do capítulo 19 tem dependências e preparação próprias.

**[COMPUTADOR]** No Windows, obtenha o **Python Install Manager**, o gerenciador oficial de instalação, pela [página de downloads do Python](https://www.python.org/downloads/). Depois de instalá-lo, abra o PowerShell, pesquisando esse nome no menu Iniciar. Digite um comando por vez e pressione Enter:

```text
py install 3.12
py -V:3.12 --version
```

**[CONSULTA]** O primeiro instala a série 3.12; o segundo deve mostrar `Python 3.12` seguido do número da atualização. Se o comando `py` não for reconhecido ou pertencer a uma instalação anterior, consulte a [orientação oficial para Windows](https://docs.python.org/3/using/windows.html), que distingue o gerenciador atual do inicializador antigo. O procedimento de instalação acima se apoia nessa documentação; não foi reproduzido nesta edição em um Windows sem Python.

**[COMPUTADOR]** No macOS e no Linux, siga a instalação correspondente ao sistema: [Python no macOS](https://docs.python.org/3.12/using/mac.html) e [Python em sistemas Unix](https://docs.python.org/3.12/using/unix.html). Confira a versão com `python3 --version`. Esses sistemas podem ter um Python usado por outros programas; mantenha essa instalação e escolha separadamente a que usará para estudar.

O livro escreve `python` nos comandos de execução. Use esse nome se `python --version` identificar a instalação escolhida. No Windows, você pode substituí-lo por `py -V:3.12`; no macOS ou Linux, por `python3`, depois de conferir a versão. Por exemplo, `python inicial.py` pode ser executado como `py -V:3.12 inicial.py` no Windows. Essa substituição vale também para comandos com `-m` e `-c`.

### Abrir a pasta certa e fazer uma primeira conferência

**[COMPUTADOR]** No Windows, abra a pasta extraída **`sem-medo-de-programar-com-ia/codigos/capitulo-04`** no Explorador de Arquivos. Copie o endereço dessa pasta pela barra de endereços. No PowerShell, digite `cd`, um espaço e esse endereço entre aspas. Por exemplo, se você extraiu o pacote em Downloads, substitua o endereço abaixo pelo seu:

```text
cd "C:\Users\SeuNome\Downloads\livros-main\sem-medo-de-programar-com-ia\codigos\capitulo-04"
py -V:3.12 inicial.py
```

`cd` muda a pasta de trabalho do terminal. O segundo comando executa o arquivo **`inicial.py`** dessa pasta. Ele deve mostrar três cadastros, inclusive dois títulos sem conteúdo visível: esse é o defeito intencional que corrigiremos no capítulo 4. Por enquanto, basta conferir que houve saída. Você pode deixar essa preparação para quando chegar à prática.

Se aparecer “arquivo não encontrado”, confira o endereço usado em `cd` e se o ZIP foi extraído. Se o terminal não reconhecer Python, volte à conferência da instalação. São problemas de preparação; a investigação da função começa depois que o arquivo consegue executar.

Para editar um `.py`, abra uma cópia em um editor de texto, como o Bloco de Notas, preserve os recuos e salve com a mesma extensão. Confira que o nome não virou **`inicial.py.txt`**. Salve antes de executar de novo; o terminal usa o conteúdo gravado no arquivo.

