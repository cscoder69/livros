"""Contratos de importação antes da introdução de recorrência."""

import json
import unittest
from copy import deepcopy
from datetime import date

from persistencia import importar_json, exportar_json


class ImportacaoTests(unittest.TestCase):
    def test_terceiro_registro_invalido_preserva_destino(self):
        tarefas = [{"titulo": "Existente", "concluida": False}]
        antes = deepcopy(tarefas)
        dados = [{"titulo": str(i), "concluida": False} for i in range(3)]
        dados[2]["prioridade"] = "urgente"
        self.assertIn("registro 2", importar_json(tarefas, json.dumps(dados)))
        self.assertEqual(tarefas, antes)
        dados[2]["prioridade"] = "alta"
        self.assertIn("concluída", importar_json(tarefas, json.dumps(dados)))
        self.assertEqual(len(tarefas), 4)

    def test_recusas_estruturais(self):
        entradas = [
            '{}', '["texto"]', '[{"titulo":42,"concluida":false}]',
            '[{"titulo":"A","concluida":"sim"}]',
            '[{"titulo":"A","titulo":"B","concluida":false}]',
            '[{"titulo":"A","concluida":false,"intervalo_dias":7}]',
        ]
        for texto in entradas:
            with self.subTest(texto=texto):
                tarefas = []
                self.assertTrue(importar_json(tarefas, texto).startswith("Importação recusada"))
                self.assertEqual(tarefas, [])

    def test_exportacao_e_importacao_preservam_data(self):
        tarefas = [{"titulo": "  Revisar  ", "concluida": False,
                    "prioridade": "alta", "prazo": date(2026, 10, 20)}]
        recuperadas = []
        self.assertIn("concluída", importar_json(recuperadas, exportar_json(tarefas)))
        self.assertEqual(recuperadas, tarefas)


if __name__ == "__main__":
    unittest.main()
