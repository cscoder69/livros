from .dados import carregar_itens
from .consultas import selecionar_abertas
from .apresentacao import apresentar


def resumo(prioridade=None):
    return apresentar(selecionar_abertas(carregar_itens(), prioridade))
