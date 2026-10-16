# Tarefa — Prioridades no cadastro

Referência didática do capítulo 6. Estado: especificada, ainda não implementada neste capítulo.

## Contexto e objetivo

Base funcional: `codigos/capitulo-02/solucao.py`. As variantes com falhas do capítulo 5 não integram a base.

O organizador cadastra, lista e conclui tarefas em memória. Queremos registrar a prioridade no cadastro para uso por funcionalidades futuras.

## Regras

1. A função passa a aceitar `cadastrar_tarefa(tarefas, titulo, prioridade="media")`.
2. Título e prioridade fornecidos serão textos. Validar outros tipos não faz parte desta tarefa.
3. Prioridades aceitas: exatamente `baixa`, `media` e `alta`, em minúsculas e sem acento ou espaços adicionais.
4. Prioridade omitida usa `media`. Prioridade vazia é inválida. Não há normalização automática.
5. A validação de título do capítulo 4 permanece: texto vazio ou apenas de espaçamento é recusado. Títulos válidos são preservados como recebidos.
6. O título é validado antes da prioridade. Se ambos forem inválidos, prevalece a mensagem do título.
7. Mensagem de título inválido: `Informe um título com pelo menos um caractere que não seja espaço.`
8. Mensagem de prioridade inválida: `Prioridade inválida. Use baixa, media ou alta.`
9. Qualquer recusa preserva toda a lista, sem modificar registros existentes ou acrescentar tarefas.
10. Cadastro válido acrescenta exatamente um registro com título original, `concluida` igual a `False` e prioridade escolhida. Retorno: `Tarefa cadastrada.`

## Compatibilidade e limites

- Chamadas com apenas lista e título continuam funcionando, acrescentando prioridade padrão às novas tarefas.
- Listagem mantém formato, ordem e comportamento da base, sem mostrar prioridades.
- Conclusão mantém o comportamento: duas chamadas válidas mantêm a tarefa concluída, preservando título e prioridade, quando houver.
- Registros antigos com apenas `titulo` e `concluida` continuam sendo listados e concluídos sem exigir sua modificação estrutural.
- Não há dados persistidos a migrar. Não alterar tarefas antigas para acrescentar prioridade nesta tarefa.
- Não criar edição de prioridade, filtros, ordenação, interface nova, persistência, bibliotecas externas ou dependência de serviço de IA para executar o programa.

## Critérios de aceitação

| ID | Ação ou condição | Resultado esperado |
| --- | --- | --- |
| P01 | Cadastrar título válido omitindo prioridade | Um novo registro com prioridade `media` e mensagem de sucesso. |
| P02 | Cadastrar com cada um dos três valores permitidos | Um novo registro com o valor informado e mensagem de sucesso, em cada caso. |
| P03 | Usar `urgente`, `Alta`, `" alta "`, `média` e texto vazio, separadamente | Mensagem de prioridade inválida, sem mudança na lista. |
| P04 | Usar título vazio, três espaços e tabulação com quebra de linha, separadamente, com prioridade válida | Mensagem de título inválido, sem mudança na lista. |
| P05 | Usar título vazio e prioridade `urgente` juntos | Mensagem de título inválido, sem mudança na lista. |
| P06 | Cadastrar `"  Ler livro  "` com prioridade `alta` | Registro com o título exato, prioridade `alta` e conclusão falsa. |
| P07 | Listar uma mistura de registros novos e antigos | Mesmo texto, ordem e marcas previstos pela função original; campo de prioridade não é exibido. |
| P08 | Concluir duas vezes uma tarefa nova e, em cenário separado, uma antiga | Ambas permanecem concluídas; demais campos preservados e sem acréscimo de campos a registros antigos. |
| P09 | Listar uma lista vazia ou concluir um índice inteiro fora do intervalo | Mensagens e ausência de alterações mantidas conforme a base. |

Nos casos de recusa, conferir listas vazias e listas com tarefas existentes. Na chamada válida, conferir o registro completo e a preservação dos registros anteriores. Cada valor enumerado representa uma verificação própria.

## Entrega esperada quando a implementação for autorizada

- Código alterado com escopo limitado ao cadastro e à nova prioridade.
- Explicação de como as regras foram atendidas.
- Conferência dos critérios, distinguindo resultados executados de análises ou verificações pendentes.
- Nenhuma substituição silenciosa dos critérios por regras escolhidas durante a implementação.

## Dúvidas pendentes

Nenhuma decisão bloqueadora conhecida para o escopo descrito. Novas dúvidas que afetem o comportamento devem ser apresentadas antes de serem resolvidas por suposição.
