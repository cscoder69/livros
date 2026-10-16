# Organizador — Referências dos capítulos 7 a 22

Material de estudo da primeira versão do manuscrito. Conferido localmente com Python 3.12. Não requer bibliotecas externas, conta de serviço de IA, chave de API nem acesso à rede para executar os programas Python.

## Escolha a etapa

| Leitura | Arquivos | Uso |
| --- | --- | --- |
| Capítulo 7 | `etapa05.py`, `capitulo-05.ipynb` | Prioridades, compatibilidade e filtros. |
| Capítulo 8 | `etapa06.py`, `capitulo-06.ipynb` | Cadastro com prazo e classificação correta de atraso. |
| Capítulo 9 | `erro_atraso.py`, `capitulo-07.ipynb` | Comparação de uma função incorreta de propósito com a correta. |
| Capítulo 11 | `test_etapa06.py`, `capitulo-08.ipynb` | Oito testes sobre os recursos ensinados até esta etapa, com as mesmas classes no arquivo de código e no arquivo local. |
| Capítulo 12 | `etapa09/` | Mesmas regras da etapa06, listagem separada e oito testes que examinam os módulos refatorados. |
| Capítulo 13 | `etapa10/`, `capitulo-10.ipynb` | Importação e exportação sem os campos de recorrência de capítulos posteriores. |
| Capítulo 14 | `dominio.py`, `organizador-final.ipynb` | Recorrência por dias e geração única da próxima ocorrência. |
| Capítulo 15 | Código final, `consultar_contexto.py` e documentos de contexto | Busca local com indicação de origem e preparação da retomada. |
| Capítulo 17, cenário local | `verificar_bissexto.py` | Conferência local bissexta; o laboratório completo do agente está em outro grupo de materiais. |
| Capítulo 18 | `materiais/capitulo-14/contrato-consulta.md`, na raiz do livro | Contrato de consulta; não configura MCP. |
| Capítulo 20 | Código final e instruções do exercício | Divisão de trabalho e conferência de integração. |
| Capítulo 21 | `materiais/capitulo-16/roteiro-de-automacao.md`, na raiz do livro | Procedimento manual e ficha; não instala agendamento. |
| Capítulo 22 | `demo.py`, suíte local e arquivo de código final | Percurso de integração e entrega. |

A versão modular inclui os recursos finais. Ela não representa o estado do projeto antes da introdução desses recursos. As etapas 5 e 6 são cópias didáticas independentes para preservar a progressão. A reorganização dos capítulos avançados não renomeou essas etapas nem os arquivos de código; o mapa acima identifica a leitura atual. Os caminhos de materiais complementares se referem ao pacote completo do livro, não apenas ao ZIP de código.

As pastas `etapa09` e `etapa10` também são versões separadas. Execute seus testes em processos próprios, dentro de cada pasta, para não misturar módulos de mesmo nome. O capítulo 13 tem três testes locais adicionais. As duas suítes da pasta principal continuam somando 23 testes.

## Pelo navegador

Abra [Google Colab](https://colab.research.google.com/) e use a opção de envio do arquivo de código. Escolha o arquivo `.ipynb` da etapa. Cada arquivo de código contém suas próprias definições e pode executar sem importar os arquivos `.py` do computador.

Execute de cima para baixo. Depois de editar uma definição, execute essa célula e as seguintes novamente. Reinicie a sessão e execute tudo em ordem para conferir uma execução limpa. Salve ou baixe sua cópia. As listas não persistem entre sessões.

As células foram executadas em Python local. **A conferência da importação e execução na interface hospedada do Colab continua pendente antes da publicação.**

## No computador

Abra um terminal na pasta destes arquivos, com Python instalado, e execute:

```text
python demo.py
python -m unittest -v test_organizador.py
```

Para conferir somente a etapa do capítulo 11, execute `python -m unittest -v test_etapa06.py`. Essa suíte usa `etapa06.py` e não importa a referência final com recorrência e importação.

`etapa05.py` e `etapa06.py` contêm definições, sem uma demonstração automática ao serem executadas diretamente. Para experimentar essas etapas no navegador, use os arquivos `.ipynb` indicados na tabela; no computador, importe as funções em uma sessão Python.

## Saída da demonstração final

```text
Tarefa cadastrada.
Tarefa cadastrada.
Abertas de prioridade alta: 1
Importação concluída: 2 tarefa(s).
Tarefa concluída.
Tarefa concluída.
0: [ ] Ler capítulo
1: [x] Revisar projeto
2: [ ] Revisar projeto
Próximo prazo: 2026-10-21
Primeira ocorrência atrasada após concluir: False
```

## Contratos e limites

- Títulos válidos são preservados; prioridades aceitas são exatamente `baixa`, `media` e `alta`.
- Prazo omitido é `None`; prazo informado usa texto `AAAA-MM-DD` no cadastro e um objeto `date` na memória.
- Filtros devolvem cópias e consideram `media` para registros antigos sem prioridade.
- Atraso recebe explicitamente a data de referência; vence hoje não é atrasada.
- Recorrência usa intervalo inteiro de 1 a 999999999 dias, dentro do limite de representação usado pela biblioteca. O próximo prazo também precisa caber no calendário; caso contrário, a conclusão é recusada sem alterações.
- Não há repetição mensal, reabertura de recorrentes nem geração de todas as ocorrências passadas.
- A geração única considera a mesma ocorrência no estado mantido pelo programa. A importação não elimina duplicatas nem sincroniza cópias dos dados.
- A importação exige lista de objetos com título e conclusão. Aceita campos opcionais de prioridade, prazo e recorrência conforme o código; recusa chaves duplicadas e campos desconhecidos.
- Registros concluídos importados não geram próximas tarefas ao serem concluídos novamente. O histórico de geração pode ser preservado no marcador `proxima_gerada`.
- Exportar devolve texto JSON. Não grava arquivo automaticamente.
- Os exemplos não implementam interface gráfica, autenticação, acesso concorrente, publicação ou servidor MCP.

O arquivo `erro_atraso.py` é intencionalmente defeituoso e nunca é a solução recomendada.

Para o cenário complementar do capítulo 17, execute `python verificar_bissexto.py` na pasta principal. Ele usa a referência final e confere datas, quantidades e preservação da lista ao repetir a conclusão. Não acrescenta métodos à suíte de 23 testes, não instala agente e não configura MCP. No arquivo de código final, o mesmo percurso pode ser experimentado com as funções já definidas.

## O que os testes demonstram

A suíte verifica contratos de prioridades, cópias de filtros, datas, atraso, preservação em recusas, importação integral e recorrência, além de uma integração de exportação/importação. Ela também verifica que o caso de fronteira distingue a função defeituosa. Isso não significa que a função defeituosa deva ser incorporada.

O pacote tem dados apenas em memória. Para estudar gravação em disco ou serviços remotos, defina antes novos critérios e limites.

## Busca local do capítulo 15

Na pasta principal, execute `python consultar_contexto.py proxima_gerada` e depois `python consultar_contexto.py concluir_tarefa`. O script mostra correspondências em dominio.py, persistencia.py e test_organizador.py, com arquivo e linha. Não altera arquivos, interpreta o significado ou consulta um modelo. Não depende da pasta em que o terminal começou para localizar esses três arquivos: usa sua própria localização. Sem correspondências não significa ausência em todo o projeto. Leia os blocos completos e confronte a regra R03; o roteiro complementar fica em materiais/capitulo-12, no pacote completo do livro.

## Novos grupos na sequência atual

Capítulo 16 usa ../projeto-existente; capítulo 17 inclui ../laboratorio-agente; capítulo 19 usa ../integracao-mcp. Cada grupo tem guia próprio. Os nomes capitulo-05.ipynb até capitulo-10.ipynb e as etapas 05/06/09/10 são históricos: acompanhe as leituras atuais 7/8/9/11/12/13 conforme a tabela deste guia. O arquivo de código final corresponde à referência introduzida no capítulo 14.
