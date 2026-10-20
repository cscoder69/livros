"""Oito testes dos recursos ensinados até o capítulo 8, sem módulos posteriores."""

import unittest
from copy import deepcopy
from datetime import date

from etapa08 import (
    cadastrar_tarefa, concluir_tarefa, esta_atrasada,
    filtrar_tarefas, interpretar_prazo, listar_tarefas,
)


class CadastroTests(unittest.TestCase):
    def test_titulo_vazio_preserva_lista(self):
        tarefas = [{"titulo": "Existente", "concluida": False}]
        antes = deepcopy(tarefas)
        mensagem = cadastrar_tarefa(tarefas, "", prioridade="alta")
        self.assertEqual(mensagem, "Informe um título com pelo menos um caractere que não seja espaço.")
        self.assertEqual(tarefas, antes)

    def test_prioridade_padrao_e_titulo_preservado(self):
        tarefas = []
        self.assertEqual(cadastrar_tarefa(tarefas, "  Ler  "), "Tarefa cadastrada.")
        self.assertEqual(tarefas, [{
            "titulo": "  Ler  ", "concluida": False, "prioridade": "media", "prazo": None,
        }])

    def test_recusas_e_ordem_das_validacoes(self):
        casos = [("", "urgente", "2026-02-30", "Informe")]
        casos += [("Válida", p, None, "Prioridade") for p in ("urgente", "Alta", " alta ", "")]
        casos += [("Válida", "alta", p, "Prazo") for p in ("", "2026-02-30", "20261014")]
        for titulo, prioridade, prazo, prefixo in casos:
            with self.subTest(titulo=titulo, prioridade=prioridade, prazo=prazo):
                tarefas = [{"titulo": "Existente", "concluida": False}]
                antes = deepcopy(tarefas)
                self.assertTrue(cadastrar_tarefa(tarefas, titulo, prioridade, prazo).startswith(prefixo))
                self.assertEqual(tarefas, antes)


class FiltrosTests(unittest.TestCase):
    def test_condicoes_ordem_e_copias(self):
        tarefas = [
            {"titulo": "Antiga", "concluida": False},
            {"titulo": "Alta aberta", "concluida": False, "prioridade": "alta"},
            {"titulo": "Alta concluída", "concluida": True, "prioridade": "alta"},
        ]
        antes = deepcopy(tarefas)
        self.assertEqual(len(filtrar_tarefas(tarefas, "alta")), 2)
        self.assertEqual(len(filtrar_tarefas(tarefas, concluida=False)), 2)
        resultado = filtrar_tarefas(tarefas, "alta", False)
        self.assertEqual([t["titulo"] for t in resultado], ["Alta aberta"])
        resultado[0]["titulo"] = "Alterado na cópia"
        self.assertEqual(tarefas, antes)
        self.assertEqual(filtrar_tarefas(tarefas, "media"), [tarefas[0]])
        self.assertEqual(filtrar_tarefas(tarefas), tarefas)
        with self.assertRaises(ValueError):
            filtrar_tarefas(tarefas, "urgente")
        with self.assertRaises(ValueError):
            filtrar_tarefas(tarefas, concluida="sim")


class PrazosTests(unittest.TestCase):
    def test_interpretacao_e_formato_exato(self):
        self.assertIsNone(interpretar_prazo(None))
        self.assertEqual(interpretar_prazo("2024-02-29"), date(2024, 2, 29))
        for entrada in ("2026-02-29", "20261014", "14/10/2026", "", 42):
            with self.subTest(entrada=entrada), self.assertRaises(ValueError):
                interpretar_prazo(entrada)

    def test_fronteiras_de_atraso(self):
        hoje = date(2026, 10, 14)
        for prazo, concluida, esperado in (
            (date(2026, 10, 13), False, True),
            (hoje, False, False),
            (date(2026, 10, 15), False, False),
            (date(2026, 10, 13), True, False),
            (None, False, False),
        ):
            with self.subTest(prazo=prazo, concluida=concluida):
                self.assertIs(esta_atrasada({"prazo": prazo, "concluida": concluida}, hoje), esperado)

    def test_cadastro_com_data_valida(self):
        tarefas = []
        self.assertEqual(cadastrar_tarefa(tarefas, "Revisar", "alta", "2026-10-14"),
                         "Tarefa cadastrada.")
        self.assertEqual(tarefas[0]["prazo"], date(2026, 10, 14))


class ApresentacaoTests(unittest.TestCase):
    def test_listagem_e_conclusao_preservadas(self):
        tarefas = [{"titulo": "Antiga", "concluida": False}]
        cadastrar_tarefa(tarefas, "Nova", "alta")
        self.assertEqual(listar_tarefas(tarefas), "0: [ ] Antiga\n1: [ ] Nova")
        for indice in (0, 1):
            concluir_tarefa(tarefas, indice)
            concluir_tarefa(tarefas, indice)
            self.assertIs(tarefas[indice]["concluida"], True)
        self.assertNotIn("prioridade", tarefas[0])
        self.assertEqual(tarefas[1]["prioridade"], "alta")
        antes = deepcopy(tarefas)
        self.assertEqual(concluir_tarefa(tarefas, 2), "Tarefa não encontrada.")
        self.assertEqual(tarefas, antes)
        self.assertEqual(listar_tarefas([]), "Nenhuma tarefa cadastrada.")


if __name__ == "__main__":
    unittest.main()
