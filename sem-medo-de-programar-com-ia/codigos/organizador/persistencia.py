"""Importação/exportação de texto JSON; não grava arquivos por conta própria."""

import json

from dominio import cadastrar_tarefa

LIMITE_BYTES = 256000
LIMITE_REGISTROS = 1000
CAMPOS = {"titulo", "concluida", "prioridade", "prazo", "intervalo_dias", "proxima_gerada"}


def objeto_sem_chaves_duplicadas(pares):
    objeto = {}
    for chave, valor in pares:
        if chave in objeto:
            raise ValueError(f"Chave duplicada: {chave}.")
        objeto[chave] = valor
    return objeto


def validar_registro(registro):
    if not isinstance(registro, dict):
        raise ValueError("Cada tarefa deve ser um objeto.")
    if set(registro) - CAMPOS:
        raise ValueError("Campos desconhecidos.")
    if "titulo" not in registro or "concluida" not in registro:
        raise ValueError("Título e conclusão são obrigatórios.")
    if type(registro["concluida"]) is not bool:
        raise ValueError("Conclusão deve ser booleana.")
    if "proxima_gerada" in registro and type(registro["proxima_gerada"]) is not bool:
        raise ValueError("Marcador de próxima ocorrência deve ser booleano.")
    temporarias = []
    mensagem = cadastrar_tarefa(
        temporarias,
        registro["titulo"],
        prioridade=registro.get("prioridade", "media"),
        prazo=registro.get("prazo"),
        intervalo_dias=registro.get("intervalo_dias"),
    )
    if mensagem != "Tarefa cadastrada.":
        raise ValueError(mensagem)
    tarefa = temporarias[0]
    tarefa["concluida"] = registro["concluida"]
    if "proxima_gerada" in registro:
        if "intervalo_dias" not in tarefa:
            raise ValueError("Marcador de recorrência em tarefa comum.")
        if registro["proxima_gerada"] and not tarefa["concluida"]:
            raise ValueError("Ocorrência aberta não pode ter gerado a próxima.")
        tarefa["proxima_gerada"] = registro["proxima_gerada"]
    return tarefa


def importar_json(tarefas, texto):
    if not isinstance(texto, str):
        return "Importação recusada: forneça texto JSON."
    try:
        tamanho = len(texto.encode("utf-8"))
    except UnicodeError:
        return "Importação recusada: texto Unicode inválido."
    if tamanho > LIMITE_BYTES:
        return "Importação recusada: limite de tamanho excedido."
    try:
        registros = json.loads(texto, object_pairs_hook=objeto_sem_chaves_duplicadas)
    except (ValueError, RecursionError):
        return "Importação recusada: JSON inválido ou chave duplicada."
    if not isinstance(registros, list) or len(registros) > LIMITE_REGISTROS:
        return "Importação recusada: use uma lista com até 1000 registros."
    temporarias = []
    for indice, registro in enumerate(registros):
        try:
            temporarias.append(validar_registro(registro))
        except ValueError as erro:
            return f"Importação recusada no registro {indice}: {erro}"
    tarefas.extend(temporarias)
    return f"Importação concluída: {len(temporarias)} tarefa(s)."


def exportar_json(tarefas):
    registros = []
    for tarefa in tarefas:
        registro = dict(tarefa)
        prazo = registro.get("prazo")
        if prazo is not None:
            registro["prazo"] = prazo.isoformat()
        registros.append(registro)
    return json.dumps(registros, ensure_ascii=False, indent=2, allow_nan=False)
