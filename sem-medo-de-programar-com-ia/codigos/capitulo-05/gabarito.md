# Gabarito — Avaliar as propostas

Leia depois da sua tentativa.

1. A preservação exata do título válido distingue A de B. A proposta A remove espaçamento nas extremidades antes do armazenamento; B apenas usa o texto tratado na condição.
2. Com `"  Ler livro  "`, A armazena `"Ler livro"` e B armazena `"  Ler livro  "`. Ambas aceitam o título sem espaços nas extremidades e recusam os três exemplos de entrada inválida.
3. A variante `cadastrar_antes_de_validar` devolve a mensagem de erro para o título vazio, mas acrescenta uma tarefa antes de verificá-lo. A lista deixa de estar vazia e contém um registro com título vazio.
4. A conclusão original permanece verdadeira após duas chamadas. A alternância termina falsa. Uma chamada isolada não mostra a diferença. A alternância está fora do escopo da validação de títulos.
5. A proposta B atende aos critérios definidos para o cadastro nos cenários examinados. A precisa de ajuste. Isso não permite afirmar que todo o projeto está livre de defeitos ou que foram avaliadas entradas de outros tipos.

Cada observação do cadastro começa com uma tarefa existente. Quantidades esperadas para as cinco entradas da tabela: **2, 1, 1, 1, 2**, em ambas as propostas. Nos três casos de recusa, `lista_preservada` deve ser `True`. A diferença entre A e B está no texto armazenado no último caso.

O sucesso de `verificar.py` significa que os comportamentos previstos foram reproduzidos, incluindo os erros intencionais. Não significa que todas as funções apresentadas devam ser incorporadas ao projeto.

## Caso adicional criado pelo leitor

O exercício revisado pede um caso próprio dentro das regras existentes. Por exemplo, `"  Estudar Python  "` distingue A de B da mesma forma que o título do livro. Antes de executar, preveja o texto armazenado: sem espaços nas extremidades em A e com os espaços preservados em B. Sua escolha pode ser outra; avalie se o resultado esperado decorre de um critério declarado.
