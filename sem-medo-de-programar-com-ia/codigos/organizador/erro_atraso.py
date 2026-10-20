"""Capítulo 9: variante incorreta de propósito; não usar como solução."""


def esta_atrasada_com_erro(tarefa, hoje):
    prazo = tarefa.get("prazo")
    return (
        not tarefa["concluida"]
        and prazo is not None
        and prazo <= hoje
    )
