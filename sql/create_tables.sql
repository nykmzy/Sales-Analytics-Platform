CREATE TABLE dim_cliente (
    cliente_id INT PRIMARY KEY,
    nome TEXT,
    idade INT,
    cidade TEXT,
    estado TEXT,
    data_cadastro DATE
);

CREATE TABLE dim_produto (
    produto_id INT PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco NUMERIC
);

CREATE TABLE dim_tempo (
    data_id SERIAL PRIMARY KEY,
    data DATE UNIQUE,
    ano INT,
    mes INT,
    dia INT,
    trimestre INT
);

CREATE TABLE fato_vendas (
    venda_id SERIAL PRIMARY KEY,
    cliente_id INT,
    produto_id INT,
    data DATE,
    quantidade INT,
    preco_unitario NUMERIC,
    valor_total NUMERIC,
    FOREIGN KEY (cliente_id) REFERENCES dim_cliente(cliente_id),
    FOREIGN KEY (produto_id) REFERENCES dim_produto(produto_id)
);

SELECT version();