from extract import extract_csv
from transform import limpar_clientes, limpar_produtos, limpar_pedidos
from load import save_processed

def run_pipeline():

    clientes = extract_csv("dataset/raw/clientes.csv")
    produtos = extract_csv("dataset/raw/produtos.csv")
    pedidos = extract_csv("dataset/raw/pedidos.csv")

    clientes_clean = limpar_clientes(clientes)
    produtos_clean = limpar_produtos(produtos)
    pedidos_clean = limpar_pedidos(pedidos)

    save_processed(clientes_clean, "clientes")
    save_processed(produtos_clean, "produtos")
    save_processed(pedidos_clean, "pedidos")

    print("Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()