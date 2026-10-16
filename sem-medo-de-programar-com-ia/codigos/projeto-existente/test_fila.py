import unittest
from fila.consultas import selecionar_abertas
from fila.servico import resumo


class FilaTests(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertEqual(selecionar_abertas([], "alta"), [])

    def test_sem_filtro(self):
        itens = [{"codigo": "X", "status": "aberta"},
                 {"codigo": "Y", "status": "encerrada"}]
        self.assertEqual([i["codigo"] for i in selecionar_abertas(itens)], ["X"])

    def test_prioridade_invalida(self):
        with self.assertRaises(ValueError):
            selecionar_abertas([], "urgente")

    def test_resumo_sem_filtro(self):
        self.assertEqual(resumo(), "Abertas: 2\nA1: Revisar contrato\nA3: Ler documentação")
