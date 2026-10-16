# Contrato de consulta — Exercício do capítulo 18

Modelo de projeto para integração futura. Não é uma configuração MCP nem um registro de conexão executada.

## Objetivo e base

Consultar tarefas usando as regras de `filtrar_tarefas`, na referência final do organizador. A camada de integração deverá preservar o contrato e o estado da origem.

## Entrada e saída propostas

- Prioridade opcional: exatamente `baixa`, `media` ou `alta`.
- Conclusão opcional: booleano. Omissão de cada condição significa ausência daquela restrição.
- Condições combinadas por “e”; ordem de origem preservada.
- Registro antigo sem prioridade é consultado como `media`, sem migração.
- Resposta com registros independentes da origem; título válido preservado.
- Prazo representado como texto `AAAA-MM-DD` ou nulo na mensagem; na origem continua `date` ou `None`.
- Sucesso sem correspondências é diferente de erro de entrada ou falha de acesso/comunicação.
- A ferramenta proposta não cadastra, conclui ou importa tarefas.

## Tabela de revisão

| Caso | Expectativa | Responsabilidade a conferir |
| --- | --- | --- |
| Alta e aberta em três registros que distinguem os filtros | Só a tarefa alta e aberta. | Regra do filtro e passagem dos parâmetros. |
| Consulta válida sem correspondências | Sucesso com nenhum registro. | Resultado da operação e relato da aplicação. |
| Prioridade `urgente` | Erro de entrada, sem alteração da origem. | Validação da interface e da operação. |
| Registro antigo, consulta por `media` | Registro selecionado sem acrescentar campo na origem. | Compatibilidade do filtro. |
| Prazo no resultado convertido para texto | Origem permanece com data. | Preparação da resposta sobre cópias. |
| Título com espaços nas extremidades | Texto exato preservado. | Preparação e apresentação da resposta. |
| Título pedindo acesso a outros arquivos | Conteúdo tratado como dado. | Aplicação, autorização e limites efetivos. |
| Servidor indisponível | Falha relatada; não afirmar lista vazia. | Comunicação e interpretação do resultado. |

## Decisões para uma implementação futura

Identificar aplicação hospedeira, SDK, versão do protocolo, transporte, autenticação aplicável e política de acesso. Relacionar a entrada e a saída propostas aos esquemas da versão escolhida. Conferir a integração e registrar ambiente, chamada, resposta e efeito observado antes de declarar conexão validada.
