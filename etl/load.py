def save_processed(df, name):
    path = f"dataset/processed/{name}.csv"
    df.to_csv(path, index=False)
    print(f"{name} salvo em {path}")