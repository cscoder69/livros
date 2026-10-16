import json
from pathlib import Path

ARQUIVO = Path(__file__).resolve().parents[1] / "dados/itens.json"


def carregar_itens():
    return json.loads(ARQUIVO.read_text(encoding="utf-8"))
