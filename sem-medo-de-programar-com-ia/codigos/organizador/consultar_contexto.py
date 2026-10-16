"""Busca lexical de estudo: mostra origem sem interpretar ou alterar o código."""

from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parent
ARQUIVOS = ("dominio.py", "persistencia.py", "test_organizador.py")


def consultar(termo):
    if not termo.strip():
        raise ValueError("Informe um termo de busca com conteúdo.")
    resultados = []
    for nome in ARQUIVOS:
        linhas = (RAIZ / nome).read_text(encoding="utf-8").splitlines()
        for numero, linha in enumerate(linhas, 1):
            if termo in linha:
                resultados.append(f"{nome}:{numero}: {linha.strip()}")
    return resultados


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].strip():
        raise SystemExit("Uso: python consultar_contexto.py termo")
    encontrados = consultar(sys.argv[1])
    print("\n".join(encontrados) if encontrados else
          "Sem correspondências nos três arquivos selecionados.")
