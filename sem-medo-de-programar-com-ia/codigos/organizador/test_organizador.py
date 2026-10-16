"""Testes de contratos e integração da referência didática."""

import json
import unittest
from copy import deepcopy
from datetime import date

import etapa05
import etapa06
from dominio import (
    cadastrar_tarefa, concluir_tarefa, esta_atrasada, filtrar_tarefas, interpretar_prazo,
)
from apresentacao import listar_tarefas
from persistencia import exportar_json, importar_json, LIMITE_BYTES
from erro_atraso import esta_atrasada_com_erro


class PrioridadesTests(unittest.TestCase):
    def test_padrao_e_valores_permitidos(self):
        for modulo in (etapa05, etapa06):
            for prioridade in (None, "baixa", "media", "alta"):
                with self.subTest(modulo=modulo.__name__, prioridade=prioridade):
                    tarefas = [{"titulo": "Antiga", "concluida": False}]
                    antes = deepcopy(tarefas)
                    kwargs = {} if prioridade is None else {"prioridade": prioridade}
                    self.assertEqual(modulo.cadastrar_tarefa(tarefas, "  Ler  ", **kwargs),
                                     "Tarefa cadastrada.")
                    self.assertEqual(tarefas[:-1], antes)
                    self.assertEqual(tarefas[-1]["titulo"], "  Ler  ")
                    self.assertEqual(tarefas[-1]["prioridade"], prioridade or "media")
                    self.assertIs(tarefas[-1]["concluida"], False)

    def test_recusas_preservam_lista_e_ordem_de_validacao(self):
        for cadastrar in (etapa05.cadastrar_tarefa, etapa06.cadastrar_tarefa, cadastrar_tarefa):
            for inicial in ([], [{"titulo": "Antiga", "concluida": True}]):
                for titulo, prioridade, prefixo in (
                    ("", "alta", "Informe"), ("   ", "alta", "Informe"),
                    ("\t\n", "alta", "Informe"), ("", "urgente", "Informe"),
                    *[("Válida", valor, "Prioridade") for valor in
                      ("urgente", "Alta", " alta ", "média", "")],
                ):
                    tarefas = deepcopy(inicial)
                    self.assertTrue(cadastrar(tarefas, titulo, prioridade).startswith(prefixo))
                    self.assertEqual(tarefas, inicial)

    def test_listagem_e_conclusao_de_antigas_e_novas(self):
        for modulo in (etapa05, etapa06):
            tarefas = [{"titulo": "Antiga", "concluida": False}]
            modulo.cadastrar_tarefa(tarefas, "Nova", "alta")
            self.assertEqual(modulo.listar_tarefas(tarefas), "0: [ ] Antiga\n1: [ ] Nova")
            for indice in (0, 1):
                modulo.concluir_tarefa(tarefas, indice)
                modulo.concluir_tarefa(tarefas, indice)
                self.assertIs(tarefas[indice]["concluida"], True)
            self.assertNotIn("prioridade", tarefas[0])
            self.assertEqual(tarefas[1]["prioridade"], "alta")
            antes = deepcopy(tarefas)
            for indice in (-1, 2):
                self.assertEqual(modulo.concluir_tarefa(tarefas, indice), "Tarefa não encontrada.")
                self.assertEqual(tarefas, antes)
            self.assertEqual(modulo.listar_tarefas([]), "Nenhuma tarefa cadastrada.")


class FiltrosTests(unittest.TestCase):
    def test_combinacao_ordem_e_copias(self):
        for filtrar in (etapa05.filtrar_tarefas, etapa06.filtrar_tarefas, filtrar_tarefas):
            tarefas = [
                {"titulo": "Antiga", "concluida": False},
                {"titulo": "Alta aberta", "concluida": False, "prioridade": "alta"},
                {"titulo": "Alta fechada", "concluida": True, "prioridade": "alta"},
            ]
            antes = deepcopy(tarefas)
            self.assertEqual(len(filtrar(tarefas, "alta")), 2)
            self.assertEqual(len(filtrar(tarefas, concluida=False)), 2)
            self.assertEqual([t["titulo"] for t in filtrar(tarefas, "alta", False)], ["Alta aberta"])
            self.assertEqual(filtrar(tarefas, "media")[0]["titulo"], "Antiga")
            resultado = filtrar(tarefas)
            self.assertEqual(resultado, tarefas)
            resultado[0]["titulo"] = "Mudou só na cópia"
            self.assertEqual(tarefas, antes)
            with self.assertRaises(ValueError):
                filtrar(tarefas, "urgente")
            with self.assertRaises(ValueError):
                filtrar(tarefas, concluida="sim")


class PrazosTests(unittest.TestCase):
    def test_formatos_e_calendario(self):
        for interpretar in (etapa06.interpretar_prazo, interpretar_prazo):
            self.assertIsNone(interpretar(None))
            self.assertEqual(interpretar("2024-02-29"), date(2024, 2, 29))
            for texto in ("2026-02-30", "2026-02-29", "20261014", "14/10/2026", "", 42):
                with self.subTest(texto=texto), self.assertRaises(ValueError):
                    interpretar(texto)

    def test_prazo_invalido_nao_cadastra(self):
        for cadastrar in (etapa06.cadastrar_tarefa, cadastrar_tarefa):
            tarefas = [{"titulo": "Antiga", "concluida": False}]
            antes = deepcopy(tarefas)
            self.assertTrue(cadastrar(tarefas, "Nova", prazo="2026-02-30").startswith("Prazo"))
            self.assertEqual(tarefas, antes)

    def test_fronteiras_de_atraso(self):
        hoje = date(2026, 10, 14)
        for classificar in (etapa06.esta_atrasada, esta_atrasada):
            for prazo, concluida, esperado in (
                (date(2026, 10, 13), False, True),
                (hoje, False, False), (date(2026, 10, 15), False, False),
                (date(2026, 10, 13), True, False), (None, False, False),
            ):
                self.assertIs(classificar({"prazo": prazo, "concluida": concluida}, hoje), esperado)

    def test_caso_de_fronteira_detecta_variante_defeituosa(self):
        hoje = date(2026, 10, 14)
        tarefa = {"prazo": hoje, "concluida": False}
        self.assertIs(esta_atrasada_com_erro(tarefa, hoje), True)
        self.assertIs(esta_atrasada(tarefa, hoje), False)


class ImportacaoTests(unittest.TestCase):
    def test_falha_no_terceiro_nao_importa_parcialmente(self):
        tarefas = [{"titulo": "Existente", "concluida": False}]
        antes = deepcopy(tarefas)
        registros = [{"titulo": str(i), "concluida": False} for i in range(3)]
        registros[2]["prioridade"] = "urgente"
        self.assertIn("registro 2", importar_json(tarefas, json.dumps(registros)))
        self.assertEqual(tarefas, antes)
        registros[2]["prioridade"] = "alta"
        self.assertIn("concluída", importar_json(tarefas, json.dumps(registros)))
        self.assertEqual(len(tarefas), 4)
        self.assertEqual(tarefas[0], antes[0])

    def test_entradas_estruturais_invalidas(self):
        entradas = [
            '{}', '["texto"]', '[{"titulo":"A","concluida":"sim"}]',
            '[{"titulo":"A","concluida":false,"extra":1}]',
            '[{"titulo":"A","titulo":"B","concluida":false}]',
            '[{"titulo":42,"concluida":false}]',
            '[{"titulo":"A","concluida":false,"prioridade":[]}]',
            '[{"titulo":"A","concluida":false,"prazo":"2026-02-30"}]',
            '[{"titulo":"A","concluida":false,"proxima_gerada":true}]',
            ' ' * (LIMITE_BYTES + 1),
            json.dumps([{"titulo":"A","concluida":False}] * 1001),
        ]
        for texto in entradas:
            with self.subTest(texto=texto[:60]):
                tarefas = []
                self.assertTrue(importar_json(tarefas, texto).startswith("Importação recusada"))
                self.assertEqual(tarefas, [])

    def test_ida_e_volta_preserva_datas_e_recorrencia(self):
        tarefas = []
        cadastrar_tarefa(tarefas, "  Revisar  ", "alta", "2026-10-14", 7)
        concluir_tarefa(tarefas, 0)
        recuperadas = []
        self.assertIn("concluída", importar_json(recuperadas, exportar_json(tarefas)))
        self.assertEqual(recuperadas, tarefas)
        concluir_tarefa(recuperadas, 0)
        self.assertEqual(len(recuperadas), 2)


class RecorrenciaTests(unittest.TestCase):
    def test_R03_geracao_unica_e_R04_cadencia(self):
        tarefas = []
        cadastrar_tarefa(tarefas, "  Revisar  ", "alta", "2026-10-14", 7)
        concluir_tarefa(tarefas, 0)
        concluir_tarefa(tarefas, 0)
        self.assertEqual(len(tarefas), 2)
        self.assertIs(tarefas[0]["concluida"], True)
        self.assertIs(tarefas[0]["proxima_gerada"], True)
        self.assertEqual(tarefas[1], {
            "titulo": "  Revisar  ", "concluida": False, "prioridade": "alta",
            "prazo": date(2026, 10, 21), "intervalo_dias": 7,
        })

    def test_R01_R02_recusas_de_recorrencia(self):
        for intervalo, prazo in ((0, "2026-10-14"), (-1, "2026-10-14"),
                                 (True, "2026-10-14"), (7, None),
                                 (1000000000, "2026-10-14")):
            tarefas = []
            self.assertNotEqual(cadastrar_tarefa(tarefas, "A", prazo=prazo,
                                                intervalo_dias=intervalo), "Tarefa cadastrada.")
            self.assertEqual(tarefas, [])

    def test_estouro_do_calendario_preserva_lista(self):
        tarefas = []
        cadastrar_tarefa(tarefas, "Limite", prazo="9999-12-31", intervalo_dias=1)
        antes = deepcopy(tarefas)
        self.assertTrue(concluir_tarefa(tarefas, 0).startswith("Próximo prazo"))
        self.assertEqual(tarefas, antes)

    def test_tarefa_comum_antiga_e_indice_invalido(self):
        tarefas = [{"titulo": "Antiga", "concluida": False}]
        concluir_tarefa(tarefas, 0)
        concluir_tarefa(tarefas, 0)
        self.assertEqual(tarefas, [{"titulo": "Antiga", "concluida": True}])
        antes = deepcopy(tarefas)
        for indice in (-1, 1, True, "0"):
            self.assertEqual(concluir_tarefa(tarefas, indice), "Tarefa não encontrada.")
            self.assertEqual(tarefas, antes)
        self.assertEqual(listar_tarefas(tarefas), "0: [x] Antiga")


if __name__ == "__main__":
    unittest.main()
