# Ficha de verificação — Exercício do capítulo 21

Modelo de preparação. Não configura uma rotina agendada ou um serviço.

## Procedimento de referência

- Gatilho inicial: solicitação manual após uma alteração na cópia de estudo.
- Entrada: identificação da cópia e pasta `codigos/organizador`.
- Comando: `python -m unittest discover -p "test_*.py" -v`.
- Quantidade esperada nesta versão: 23 métodos na pasta principal. Etapas09 e10 têm conferências próprias.
- Ação permitida: executar e relatar. Não editar, instalar dependências ou publicar.
- Resultado: registrar pasta, comando, base, quantidade executada, falhas, erros, ignorados e pendências.

## Condições de saída

| Condição | Relato | Continuação |
| --- | --- | --- |
| Métodos esperados executados e aprovados | Verificação atendida para a base identificada. | Decidir próximo trabalho no escopo autorizado. |
| Um ou mais testes falham | Identificar teste e diferença disponível. | Investigar; não reescrever automaticamente. |
| Nenhum teste descoberto | Verificação prevista não foi realizada. | Conferir pasta, padrão e arquivos. |
| Executor não iniciou | Registrar a falha de ambiente disponível. | Corrigir preparação ou manter execução pendente. |
| Dados da base mudaram durante a verificação | Identificação da evidência ficou insuficiente. | Conferir uma versão consistente antes de aprovar. |

## Observações reais

Preencher somente depois de executar: ambiente, identificação da cópia, comando, resumo, resultado e pendências. Separar casos planejados de casos observados.

## Política para configuração futura

Definir gatilho efetivo, conta de execução, acessos, limites de duração, histórico e notificações. Uma execução de testes não autoriza publicação. Uma espera sem resposta de operação que altera dados não autoriza presumir ausência do efeito e repeti-la sem conferência.
