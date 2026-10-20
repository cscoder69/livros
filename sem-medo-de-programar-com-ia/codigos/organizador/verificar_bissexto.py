"""Cenário independente do capítulo 17; não configura um agente nem MCP."""

from copy import deepcopy
from datetime import date

from dominio import cadastrar_tarefa, concluir_tarefa


def verificar():
    tarefas = []
    assert cadastrar_tarefa(tarefas, "Revisar", prioridade="alta",
                            prazo="2028-02-28", intervalo_dias=1) == "Tarefa cadastrada."
    assert concluir_tarefa(tarefas, 0) == "Tarefa concluída."
    assert len(tarefas) == 2
    assert tarefas[1]["prazo"] == date(2028, 2, 29)
    assert tarefas[1]["concluida"] is False
    antes = deepcopy(tarefas)
    assert concluir_tarefa(tarefas, 0) == "Tarefa concluída."
    assert tarefas == antes
    assert concluir_tarefa(tarefas, 1) == "Tarefa concluída."
    assert len(tarefas) == 3
    assert tarefas[2]["prazo"] == date(2028, 3, 1)
    assert tarefas[2]["concluida"] is False
    antes = deepcopy(tarefas)
    assert concluir_tarefa(tarefas, 1) == "Tarefa concluída."
    assert tarefas == antes
    print("Recorrência bissexta conferida: 2028-02-28 -> 2028-02-29 -> 2028-03-01.")


if __name__ == "__main__":
    verificar()
