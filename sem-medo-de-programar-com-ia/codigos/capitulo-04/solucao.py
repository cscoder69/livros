"""Solução de referência: valida o título antes de cadastrar."""


def cadastrar_tarefa(tarefas, titulo):
    if not titulo.strip():
        return "Informe um título com pelo menos um caractere que não seja espaço."
    tarefas.append({"titulo": titulo, "concluida": False})
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


if __name__ == "__main__":
    tarefas = []
    print(cadastrar_tarefa(tarefas, "Comprar pão"))
    print(cadastrar_tarefa(tarefas, ""))
    print(cadastrar_tarefa(tarefas, "   "))
    print(listar_tarefas(tarefas))
    print(concluir_tarefa(tarefas, 0))
    print(listar_tarefas(tarefas))
