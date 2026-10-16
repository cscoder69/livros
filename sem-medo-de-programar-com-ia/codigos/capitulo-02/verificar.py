"""Execute com Python para conferir os critérios da solução de referência."""

from copy import deepcopy

from solucao import cadastrar_tarefa, concluir_tarefa, listar_tarefas


def verificar():
    tarefas = []
    assert listar_tarefas(tarefas) == "Nenhuma tarefa cadastrada."
    assert cadastrar_tarefa(tarefas, "Comprar pão") == "Tarefa cadastrada."
    assert tarefas == [{"titulo": "Comprar pão", "concluida": False}]
    for titulo in ("", "   ", "\t\n"):
        antes = deepcopy(tarefas)
        assert cadastrar_tarefa(tarefas, titulo).startswith("Informe um título")
        assert tarefas == antes, "Uma entrada inválida modificou a lista."
    assert cadastrar_tarefa(tarefas, "  Ler livro  ") == "Tarefa cadastrada."
    assert tarefas[1]["titulo"] == "  Ler livro  ", "O título válido foi alterado."
    assert concluir_tarefa(tarefas, 0) == "Tarefa concluída."
    assert tarefas[0]["concluida"] is True
    assert tarefas[1]["concluida"] is False
    assert listar_tarefas(tarefas) == "0: [x] Comprar pão\n1: [ ]   Ler livro  "
    for indice in (-1, 2):
        antes = deepcopy(tarefas)
        assert concluir_tarefa(tarefas, indice) == "Tarefa não encontrada."
        assert tarefas == antes
    print("Verificações concluídas: cadastro, validação, listagem e conclusão.")


if __name__ == "__main__":
    verificar()
