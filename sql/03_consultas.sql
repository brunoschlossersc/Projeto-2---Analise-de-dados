-- Consultas analíticas fundamentais na tabela tratada (pós-ETL)
-- Exportação pode ser feita via DBeaver/pgAdmin ou pelo comando COPY

-- 1. Qual filial apresentou o maior faturamento?
SELECT filial, SUM(valor_total) as faturamento_total
FROM tratada_vendas
GROUP BY filial
ORDER BY faturamento_total DESC;

-- 2. Qual linha de produto recebeu a melhor avaliação média?
SELECT linha_produto, AVG(avaliacao) as avaliacao_media
FROM tratada_vendas
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;

-- 3. Em qual dia da semana ocorreu a maior quantidade de vendas? (PostgreSQL)
SELECT EXTRACT(ISODOW FROM data_venda) as dia_semana, COUNT(id_venda) as qtd_vendas
FROM tratada_vendas
GROUP BY dia_semana
ORDER BY qtd_vendas DESC;

-- Exemplo de exportação para CSV diretamente pelo banco (requer permissões):
-- COPY (SELECT * FROM tratada_vendas) TO '/caminho/do/projeto/data/raw/extracao_banco.csv' DELIMITER ',' CSV HEADER;