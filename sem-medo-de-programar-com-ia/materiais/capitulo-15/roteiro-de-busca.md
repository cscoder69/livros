# Roteiro de busca local — capítulo 15

Modelo para investigar a referência final do organizador. A busca lexical procura ocorrências do texto informado; não é uma implementação de RAG. A ferramenta consulta apenas os três arquivos indicados no capítulo; encontrar texto não decide seu significado.

## Pergunta e referência

- Pergunta: qual estado impede a geração repetida da próxima ocorrência?
- Regra vigente: R03, capítulo 14.
- Base: identificar a pasta e a versão realmente consultadas.
- Primeiros termos: `proxima_gerada` e `concluir_tarefa`.

## Registro da investigação

| Item | Preencher depois da consulta |
| --- | --- |
| Arquivo e linha encontrados | Copiar a origem da saída; a linha pode mudar entre versões. |
| Trecho completo relido | Identificar a função ou bloco, não apenas uma linha isolada. |
| Papel do marcador | Conferir onde é atribuído e onde é validado. |
| Condição de retorno | Localizar o estado consultado antes de calcular outra ocorrência. |
| Teste correspondente | Localizar o caso que conclui duas vezes e confere quantidade. |
| Execução | Anotar comando, base e resultado; manter pendente se apenas leu. |
| Conclusão | Ligar regra, trecho e evidência disponível. |

## Conferência da interpretação

Na referência atual, a decisão usa `concluida`; `proxima_gerada` registra a geração. Compare essa resposta com a função completa. Se sua cópia divergir, registre a diferença em vez de adaptar o relato silenciosamente.

Busque também um termo que não exista nesses arquivos. O resultado sem correspondências não comprova ausência em todo o projeto. Registre esse limite.

Finalize com um resumo de retomada corrigido, indicando as fontes que precisam ser relidas para uma futura alteração de recorrência. Não apresente uma inspeção por leitura como teste executado.
