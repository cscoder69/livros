"""Regras da referência final de estudo. Python 3.12, sem rede ou bibliotecas externas."""

from copy import deepcopy
from datetime import date, timedelta

ERRO_TITULO = "Informe um título com pelo menos um caractere que não seja espaço."
ERRO_PRIORIDADE = "Prioridade inválida. Use baixa, media ou alta."
PRIORIDADES = ("baixa", "media", "alta")


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


def cadastrar_tarefa(tarefas, titulo, prioridade="media", prazo=None, intervalo_dias=None):
    if not isinstance(titulo, str) or not titulo.strip():
        return ERRO_TITULO
    if prioridade not in PRIORIDADES:
        return ERRO_PRIORIDADE
    try:
        data_prazo = interpretar_prazo(prazo)
    except ValueError as erro:
        return str(erro)
    if intervalo_dias is not None:
        if type(intervalo_dias) is not int or not 1 <= intervalo_dias <= 999999999:
            return "Intervalo deve ser um inteiro positivo de até 999999999 dias."
        if data_prazo is None:
            return "Tarefa recorrente precisa de prazo."
    tarefa = {
        "titulo": titulo,
        "concluida": False,
        "prioridade": prioridade,
        "prazo": data_prazo,
    }
    if intervalo_dias is not None:
        tarefa["intervalo_dias"] = intervalo_dias
    tarefas.append(tarefa)
    return "Tarefa cadastrada."


def concluir_tarefa(tarefas, indice):
    if type(indice) is not int or indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."
    tarefa = tarefas[indice]
    if tarefa["concluida"]:
        return "Tarefa concluída."
    intervalo = tarefa.get("intervalo_dias")
    proxima = None
    if intervalo is not None:
        try:
            novo_prazo = tarefa["prazo"] + timedelta(days=intervalo)
        except (OverflowError, TypeError):
            return "Próximo prazo fora do intervalo suportado."
        proxima = {
            "titulo": tarefa["titulo"],
            "concluida": False,
            "prioridade": tarefa.get("prioridade", "media"),
            "prazo": novo_prazo,
            "intervalo_dias": intervalo,
        }
    tarefa["concluida"] = True
    if proxima is not None:
        tarefa["proxima_gerada"] = True
        tarefas.append(proxima)
    return "Tarefa concluída."


def filtrar_tarefas(tarefas, prioridade=None, concluida=None):
    if prioridade is not None and prioridade not in PRIORIDADES:
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


def esta_atrasada(tarefa, hoje):
    prazo = tarefa.get("prazo")
    return (
        not tarefa["concluida"]
        and prazo is not None
        and prazo < hoje
    )
