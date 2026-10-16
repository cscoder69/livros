import argparse
from .servico import resumo


def main():
    parser = argparse.ArgumentParser(description="Resumo da fila fictícia de atendimento.")
    parser.add_argument("--prioridade", choices=("baixa", "media", "alta"))
    args = parser.parse_args()
    print(resumo(args.prioridade))


if __name__ == "__main__":
    main()
