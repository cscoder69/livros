# Desafio final — uma alteração pequena, uma entrega completa

Prática do capítulo 22, em uma cópia de estudo. A referência distribuída mantém sua listagem original. Esta ficha propõe uma variação para o leitor implementar; não contém solução pronta nem resultados de execução.

## Pedido recebido

Mostrar a prioridade na listagem, entre a marca de conclusão e o título. Preservar a ordem das tarefas, seus índices e todos os dados de origem. Títulos válidos mantêm os espaços recebidos. Para registro antigo sem prioridade, mostrar media durante a leitura, sem acrescentar o campo ao registro.

Exemplos do formato desejado: `0: [ ] (alta) Revisar` e `1: [x] (media) Antiga`. São expectativas para os respectivos dados, não saídas já executadas nesta edição. Lista vazia conserva a mensagem anterior.

## Preparar a tarefa

- Usar uma cópia do [organizador](../../codigos/organizador/README.md) e identificar sua versão.
- Ler a função `listar_tarefas` em **`codigos/organizador/apresentacao.py`** e localizar seus usos. No arquivo **`organizador-final.ipynb`**, a mesma função fica nas células; siga a opção escolhida no capítulo 22.
- Escrever critérios de saída e de preservação dos dados.
- Definir o que fica fora: cadastro, filtros, prazos, conclusão, importação e exportação não mudam.
- Preparar o pedido à IA ou realizar diretamente a alteração e pedir revisão das diferenças.

## Conferir a entrega

Escolher dados que incluam lista vazia, prioridade alta, tarefa antiga sem prioridade, título com espaços e tarefa concluída. Anotar expectativas antes da execução. Conferir texto, ordem, índices e igualdade dos registros de origem antes/depois da listagem.

Os testes que comparavam o texto anterior precisam refletir a nova regra de apresentação, mantendo as demais verificações. Conferir quais módulos os testes chamam: uma aprovação sobre **`etapa08.py`** não examina por si só a listagem modificada em **`apresentacao.py`**. Atualize as expectativas afetadas pela nova regra e conserve as de preservação dos dados.

Repetir o percurso completo de cadastro, filtro, exportação/importação e conclusão recorrente. Comparar os dados com seus contratos; a alteração visual não autoriza mudar essas regras.

## Preparar a nota final

- Pedido interpretado e critérios escolhidos.
- Arquivos alterados e diferenças.
- Comandos, cópia, entradas e resultados reais.
- Limites e verificações ainda pendentes.
- Instruções para uma primeira execução por outra pessoa.
- Razão para aceitar, ajustar ou descartar a alteração.

Se apenas planejou, guardar a ficha como preparação e manter a implementação/execução pendentes. Se executou, conservar os registros. Para o exercício seguinte, escolher uma pequena tarefa em outro projeto e repetir o percurso sem copiar a ficha preenchida do organizador.
