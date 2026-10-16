"""Exemplos didáticos: algumas funções violam os requisitos de propósito."""

from copy import deepcopy

ERRO = "Informe um título com pelo menos um caractere que não seja espaço."
SUCESSO = "Tarefa cadastrada."
CASOS = ("Comprar pão", "", "   ", "\t\n", "  Ler livro  ")


def cadastrar_a(tarefas, titulo):
    titulo = titulo.strip()
    if not titulo:
        return ERRO
    tarefas.append({"titulo": titulo, "concluida": False})
    return SUCESSO


def cadastrar_b(tarefas, titulo):
    if not titulo.strip():
        return ERRO
    tarefas.append({"titulo": titulo, "concluida": False})
    return SUCESSO


def cadastrar_antes_de_validar(tarefas, titulo):
    tarefas.append({"titulo": titulo, "concluida": False})
    if not titulo.strip():
        return ERRO
    return SUCESSO


def concluir_original(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."
    tarefas[indice]["concluida"] = True
    return "Tarefa concluída."


def concluir_alternando(tarefas, indice):
    if indice < 0 or indice >= len(tarefas):
        return "Tarefa não encontrada."
    tarefas[indice]["concluida"] = not tarefas[indice]["concluida"]
    return "Tarefa concluída."


def observar(cadastrar, titulo):
    tarefas = [{"titulo": "Tarefa existente", "concluida": True}]
    antes = deepcopy(tarefas)
    retorno = cadastrar(tarefas, titulo)
    return {
        "retorno": retorno,
        "quantidade": len(tarefas),
        "titulos": [tarefa["titulo"] for tarefa in tarefas],
        "lista_preservada": tarefas == antes,
    }


def comparar():
    for nome, cadastrar in (("A", cadastrar_a), ("B", cadastrar_b)):
        print(f"Proposta {nome}")
        for titulo in CASOS:
            resultado = observar(cadastrar, titulo)
            print("Entrada:", repr(titulo))
            print("Retorno:", resultado["retorno"])
            print("Quantidade:", resultado["quantidade"])
            print("Títulos:", repr(resultado["titulos"]))
            print("Lista preservada:", resultado["lista_preservada"])
            print()


def demonstrar_falhas():
    tarefas = []
    print("Cadastro antes de validar:")
    print(cadastrar_antes_de_validar(tarefas, ""))
    print("Quantidade após a recusa:", len(tarefas))
    print("Conteúdo:", repr(tarefas))
    print()
    for nome, concluir in (("Original", concluir_original), ("Alternância", concluir_alternando)):
        tarefas = [{"titulo": "Comprar pão", "concluida": False}]
        concluir(tarefas, 0)
        concluir(tarefas, 0)
        print(nome, "— concluída após duas chamadas:", tarefas[0]["concluida"])


if __name__ == "__main__":
    comparar()
    demonstrar_falhas()
