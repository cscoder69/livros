def apresentar(itens):
    linhas = [f"Abertas: {len(itens)}"]
    linhas.extend(f"{item['codigo']}: {item['titulo']}" for item in itens)
    return "\n".join(linhas)
