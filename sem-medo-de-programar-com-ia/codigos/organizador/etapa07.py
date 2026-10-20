"""Capítulo 7: prioridades e filtros, com dados em memória."""

from copy import deepcopy


def cadastrar_tarefa(tarefas, titulo, prioridade="media"):
    if not titulo.strip():
        return "Informe um título com pelo menos um caractere que não seja espaço."
    if prioridade not in ("baixa", "media", "alta"):
        return "Prioridade inválida. Use baixa, media ou alta."
    tarefas.append({
        "titulo": titulo,
        "concluida": False,
        "prioridade": prioridade,
    })
    return "Tarefa cadastrada."


def concluir_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."
    tarefas[indice]["concluida"] = True
    return "Tarefa concluída."


def listar_tarefas(tarefas):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    linhas = []
    for indice, tarefa in enumerate(tarefas):
        marca = "x" if tarefa["concluida"] else " "
        linhas.append(f"{indice}: [{marca}] {tarefa['titulo']}")
    return "\n".join(linhas)


def filtrar_tarefas(tarefas, prioridade=None, concluida=None):
    if prioridade is not None and prioridade not in ("baixa", "media", "alta"):
        raise ValueError("Prioridade de filtro inválida.")
    if concluida is not None and type(concluida) is not bool:
        raise ValueError("Conclusão de filtro deve ser booleana.")
    resultado = []
    for tarefa in tarefas:
        if prioridade is not None and tarefa.get("prioridade", "media") != prioridade:
            continue
        if concluida is not None and tarefa["concluida"] != concluida:
            continue
        resultado.append(deepcopy(tarefa))
    return resultado
