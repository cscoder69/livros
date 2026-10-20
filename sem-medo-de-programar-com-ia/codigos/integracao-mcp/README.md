# Integração MCP local — capítulo 19

Python 3.12, com a biblioteca oficial `mcp` 2.3.0, parte do conjunto de componentes de desenvolvimento chamado SDK. Um programa cliente envia pedidos e outro programa, o servidor, oferece a consulta. `stdio` é a comunicação pela entrada e saída desses programas. Não exige modelo conectado, chave de API ou conta pessoal. Dados fictícios e consulta; nenhum serviço publicado.

**[COMPUTADOR]** Na pasta destes arquivos, em Windows:

```text
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe cliente_verificacao.py
```

O primeiro comando cria um ambiente virtual na pasta `.venv`, separando os pacotes desta prática; o segundo usa `pip` para instalar os componentes listados em `requirements.txt`; o terceiro executa o cliente. Essa separação de pacotes não restringe o acesso do programa aos arquivos do computador.

O cliente inicia e encerra o servidor. Executar `servidor.py` sozinho deixa-o esperando comunicação. As oito conferências cobrem descoberta, quatro consultas, duas recusas e origem preservada. A saída é JSON; erro encerra com um código de saída diferente de zero, sinal de que o percurso não terminou com sucesso. A espera é limitada a 15 segundos por pedido e 45 segundos por percurso, depois de carregar os módulos.

`base_dominio.py` é cópia da referência original. `RespostaConsulta` declara tarefas e quantidade; o cliente ainda verifica seu conteúdo. Datas são convertidas nas cópias, e ausência de prazo vira nulo. `estado://base` é o identificador de um recurso fictício do servidor, não um site: o cliente o lê antes e depois das consultas, solicitando uma resposta nova em vez de reutilizar a anterior.

`requirements.txt` fixa a dependência direta. `ambiente-validado-windows.txt` registra também as versões dos componentes instalados como dependências dela, sem prometer compatibilidade com outros sistemas. Os resultados da preparação da edição ficam no histórico editorial da revisão 09; para sua prática, registre a saída produzida pelo cliente e compare com a tabela do capítulo 19. Para outra plataforma, adapte o caminho do Python do ambiente e confira a execução. A informação descritiva de que uma ferramenta só lê dados não substitui controle de acesso; o título com frase de instrução é dado, e esta execução não testa um modelo contra injeção de prompt.
