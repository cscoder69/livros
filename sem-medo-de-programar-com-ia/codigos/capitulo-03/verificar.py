"""Confere os casos do capítulo, inclusive as falhas intencionais."""

from propostas import (
    CASOS, ERRO, SUCESSO, cadastrar_a, cadastrar_b,
    cadastrar_antes_de_validar, concluir_original, concluir_alternando, observar,
)


def verificar():
    for cadastrar in (cadastrar_a, cadastrar_b):
        for titulo in CASOS:
            resultado = observar(cadastrar, titulo)
            if not titulo.strip():
                assert resultado["retorno"] == ERRO
                assert resultado["quantidade"] == 1
                assert resultado["lista_preservada"] is True
                assert resultado["titulos"] == ["Tarefa existente"]
            else:
                assert resultado["retorno"] == SUCESSO
                assert resultado["quantidade"] == 2
                esperado = titulo.strip() if cadastrar is cadastrar_a else titulo
                assert resultado["titulos"] == ["Tarefa existente", esperado]
                assert resultado["lista_preservada"] is False
    assert observar(cadastrar_a, "  Ler livro  ")["titulos"][-1] != "  Ler livro  "
    assert observar(cadastrar_b, "  Ler livro  ")["titulos"][-1] == "  Ler livro  "
    tarefas = []
    assert cadastrar_antes_de_validar(tarefas, "") == ERRO
    assert tarefas == [{"titulo": "", "concluida": False}]
    for concluir, esperado in ((concluir_original, True), (concluir_alternando, False)):
        tarefas = [{"titulo": "Comprar pão", "concluida": False}]
        concluir(tarefas, 0)
        assert tarefas[0]["concluida"] is True
        concluir(tarefas, 0)
        assert tarefas[0]["concluida"] is esperado
    print("Conferência concluída: diferenças e falhas intencionais reproduzidas.")


if __name__ == "__main__":
    verificar()
