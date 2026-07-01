import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

def gerar_clientes(n=100):
    return pd.DataFrame({
        "cliente_id": range(1, n+1),
        "nome": [fake.name() for _ in range(n)],
        "idade": np.random.randint(18, 70, n),
        "cidade": [fake.city() for _ in range(n)],
        "estado": [fake.state_abbr() for _ in range(n)],
        "data_cadastro": [fake.date_this_year() for _ in range(n)]
    })

def gerar_produtos(n=50):
    return pd.DataFrame({
        "produto_id": range(1, n+1),
        "nome": [fake.word() for _ in range(n)],
        "categoria": np.random.choice(["Eletrônicos", "Roupas", "Casa"], n),
        "preco": np.round(np.random.uniform(10, 1000, n), 2)
    })

def gerar_pedidos(n=300):
    return pd.DataFrame({
        "pedido_id": range(1, n+1),
        "cliente_id": np.random.randint(1, 100, n),
        "produto_id": np.random.randint(1, 50, n),
        "quantidade": np.random.randint(1, 5, n),
        "data_pedido": [fake.date_this_year() for _ in range(n)]
    })

clientes = gerar_clientes()
produtos = gerar_produtos()
pedidos = gerar_pedidos()

clientes.to_csv("dataset/raw/clientes.csv", index=False)
produtos.to_csv("dataset/raw/produtos.csv", index=False)
pedidos.to_csv("dataset/raw/pedidos.csv", index=False)

print("Dados gerados com sucesso!")