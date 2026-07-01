import pandas as pd

def criar_fato_vendas(pedidos, produtos):

    # JOIN pedidos + produtos
    df = pedidos.merge(produtos, on="produto_id", how="left")

    # cálculo de métricas
    df["preco_unitario"] = df["preco"]
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]

    # seleção final da fato
    fato = df[[
        "pedido_id",
        "cliente_id",
        "produto_id",
        "data_pedido",
        "quantidade",
        "preco_unitario",
        "valor_total"
    ]].copy()

    # renomear para padrão DW
    fato.rename(columns={
        "pedido_id": "venda_id",
        "data_pedido": "data"
    }, inplace=True)

    return fato