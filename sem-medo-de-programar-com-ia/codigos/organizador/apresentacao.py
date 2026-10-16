"""Apresentação textual preservada desde o primeiro exemplo."""


def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    linhas = []
    for indice, tarefa in enumerate(tarefas):
        marca = "x" if tarefa["concluida"] else " "
        linhas.append(f"{indice}: [{marca}] {tarefa['titulo']}")
    return "\n".join(linhas)
