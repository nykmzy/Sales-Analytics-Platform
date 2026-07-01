import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

np.random.seed(42)

# -------------------------
# CLIENTES
# -------------------------
def gerar_clientes(n=200):
    return pd.DataFrame({
        "cliente_id": range(1, n+1),
        "nome": [fake.name() for _ in range(n)],
        "idade": np.random.randint(18, 75, n),
        "cidade": [fake.city() for _ in range(n)],
        "estado": [fake.state_abbr() for _ in range(n)],
        "data_cadastro": [fake.date_between("-2y", "today") for _ in range(n)]
    })

# -------------------------
# PRODUTOS
# -------------------------
def gerar_produtos(n=80):
    categorias = ["Eletrônicos", "Roupas", "Casa", "Esporte", "Alimentos"]

    return pd.DataFrame({
        "produto_id": range(1, n+1),
        "nome": [fake.word().capitalize() for _ in range(n)],
        "categoria": np.random.choice(categorias, n),
        "preco": np.round(np.random.uniform(10, 2000, n), 2)
    })

# -------------------------
# PEDIDOS (FATO BRUTA)
# -------------------------
def gerar_pedidos(n=1000, n_clientes=200, n_produtos=80):
    data_inicio = pd.to_datetime("2023-01-01")
    data_fim = pd.to_datetime("2025-12-31")

    datas = pd.date_range(data_inicio, data_fim)

    pedidos = pd.DataFrame({
        "pedido_id": range(1, n+1),
        "cliente_id": np.random.randint(1, n_clientes+1, n),
        "produto_id": np.random.randint(1, n_produtos+1, n),
        "quantidade": np.random.randint(1, 5, n),
        "data_pedido": np.random.choice(datas, n)
    })

    return pedidos


# -------------------------
# EXECUÇÃO
# -------------------------
clientes = gerar_clientes()
produtos = gerar_produtos()
pedidos = gerar_pedidos()

clientes.to_csv("dataset/raw/clientes.csv", index=False)
produtos.to_csv("dataset/raw/produtos.csv", index=False)
pedidos.to_csv("dataset/raw/pedidos.csv", index=False)

print("✅ Dados gerados com sucesso!")