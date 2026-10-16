"""Percurso completo de referência: não acessa rede nem grava arquivos."""

from datetime import date

from dominio import cadastrar_tarefa, concluir_tarefa, esta_atrasada, filtrar_tarefas
from apresentacao import listar_tarefas
from persistencia import exportar_json, importar_json


def demonstrar():
    tarefas = []
    print(cadastrar_tarefa(tarefas, "Ler capítulo", prioridade="baixa"))
    print(cadastrar_tarefa(tarefas, "Revisar projeto", prioridade="alta",
                          prazo="2026-10-14", intervalo_dias=7))
    print("Abertas de prioridade alta:", len(filtrar_tarefas(tarefas, "alta", False)))
    texto = exportar_json(tarefas)
    recuperadas = []
    print(importar_json(recuperadas, texto))
    print(concluir_tarefa(recuperadas, 1))
    print(concluir_tarefa(recuperadas, 1))
    print(listar_tarefas(recuperadas))
    print("Próximo prazo:", recuperadas[2]["prazo"].isoformat())
    print("Primeira ocorrência atrasada após concluir:",
          esta_atrasada(recuperadas[1], date(2026, 10, 17)))
    return recuperadas


if __name__ == "__main__":
    demonstrar()
