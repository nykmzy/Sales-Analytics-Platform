from etl.db import get_connection

def insert_dataframe(df, table_name):

    conn = get_connection()
    cursor = conn.cursor()

    cols = ",".join(df.columns)
    values_placeholder = ",".join(["%s"] * len(df.columns))

    query = f"""
        INSERT INTO {table_name} ({cols})
        VALUES ({values_placeholder})
    """

    for row in df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"{table_name} carregada com sucesso")