"""Capítulo 6: prioridades, filtros e prazos, com dados em memória."""

from copy import deepcopy
from datetime import date


def cadastrar_tarefa(tarefas, titulo, prioridade="media", prazo=None):
    if not titulo.strip():
        return "Informe um título com pelo menos um caractere que não seja espaço."
    if prioridade not in ("baixa", "media", "alta"):
        return "Prioridade inválida. Use baixa, media ou alta."
    try:
        data_prazo = interpretar_prazo(prazo)
    except ValueError as erro:
        return str(erro)
    tarefas.append({
        "titulo": titulo,
        "concluida": False,
        "prioridade": prioridade,
        "prazo": data_prazo,
    })
    return "Tarefa cadastrada."


def concluir_tarefa(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."
    tarefas[indice]["concluida"] = True
    return "Tarefa concluída."




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


def interpretar_prazo(texto):
    if texto is None:
        return None
    if not isinstance(texto, str):
        raise ValueError("Prazo deve ser texto no formato AAAA-MM-DD.")
    try:
        prazo = date.fromisoformat(texto)
    except ValueError:
        raise ValueError("Prazo inválido. Use AAAA-MM-DD.") from None
    if prazo.isoformat() != texto:
        raise ValueError("Prazo inválido. Use AAAA-MM-DD.")
    return prazo


def esta_atrasada(tarefa, hoje):
    prazo = tarefa.get("prazo")
    return (
        not tarefa["concluida"]
        and prazo is not None
        and prazo < hoje
    )
