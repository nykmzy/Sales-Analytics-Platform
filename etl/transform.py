def limpar_clientes(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["estado"] = df["estado"].str.upper()
    return df


def limpar_produtos(df):
    df = df.drop_duplicates()
    df = df.dropna()
    df["preco"] = df["preco"].abs()
    return df


def limpar_pedidos(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df