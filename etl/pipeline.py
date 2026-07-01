from etl.extract import extract_csv
from etl.transform import limpar_clientes, limpar_produtos, limpar_pedidos
from etl.load import insert_dataframe
from etl.fato_vendas import criar_fato_vendas

def run_pipeline():

    clientes = extract_csv("dataset/raw/clientes.csv")
    produtos = extract_csv("dataset/raw/produtos.csv")
    pedidos = extract_csv("dataset/raw/pedidos.csv")

    clientes = limpar_clientes(clientes)
    produtos = limpar_produtos(produtos)
    pedidos = limpar_pedidos(pedidos)

    insert_dataframe(clientes, "dim_cliente")
    insert_dataframe(produtos, "dim_produto")

    fato = criar_fato_vendas(pedidos, produtos)
    insert_dataframe(fato, "fato_vendas")

    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()