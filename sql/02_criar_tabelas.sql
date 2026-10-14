-- Conecte-se ao banco supermercado_db antes de executar

-- 1. Criação da Tabela Raw (Cópia fiel do CSV original, sem restrições rígidas para não quebrar a carga)
CREATE TABLE raw_vendas (
    invoice_id VARCHAR(50),
    branch VARCHAR(50),
    city VARCHAR(100),
    customer_type VARCHAR(50),
    gender VARCHAR(50),
    product_line VARCHAR(150),
    unit_price VARCHAR(50),
    quantity VARCHAR(50),
    tax_5_percent VARCHAR(50),
    total VARCHAR(50),
    date VARCHAR(50),
    time VARCHAR(50),
    payment VARCHAR(50),
    cogs VARCHAR(50),
    gross_margin_percentage VARCHAR(50),
    gross_income VARCHAR(50),
    rating VARCHAR(50)
);

-- 2. Criação da Tabela Tratada (Com base no Dicionário de Dados)
CREATE TABLE tratada_vendas (
    id_venda VARCHAR(50) PRIMARY KEY NOT NULL,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) CHECK (preco_unitario >= 0),
    quantidade INTEGER CHECK (quantidade > 0),
    imposto NUMERIC(10,2) CHECK (imposto >= 0),
    valor_total NUMERIC(12,2) CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2) CHECK (avaliacao >= 0 AND avaliacao <= 10)
);