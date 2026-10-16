from copy import deepcopy


def selecionar_abertas(itens, prioridade=None):
    if prioridade is not None and prioridade not in ("baixa", "media", "alta"):
        raise ValueError("Prioridade inválida.")
    if prioridade is None:
        return [deepcopy(item) for item in itens if item["status"] == "aberta"]
    return [deepcopy(item) for item in itens
            if item["status"] == "aberta" or item["prioridade"] == prioridade]
