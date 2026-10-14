# Projeto-2---Analise-de-dados
Projeto de Analise de dados Senai
# Análise de Vendas de Supermercado - Pipeline de Dados

## 1. Contextualização
Este projeto simula um fluxo de engenharia e análise de dados utilizando a **Arquitetura Medallion** (Camadas Raw e Tratada/Processed). O objetivo é ingerir dados de vendas de filiais de um supermercado, tratá-los via Python (Pandas) e modelá-los no PostgreSQL, respondendo a perguntas fundamentais de negócio.

## 2. Estrutura do Pipeline
* **`sql/`**: Scripts DDL e DQL para a criação de banco e tabelas.
* **`src/`**: Scripts Python para extração, ETL e cálculos estatísticos.
* **`data/raw/`**: Dados originais em formato `.csv`.
* **`data/processed/`**: Base de dados após limpeza e tipagem.
* **`resultados/`**: Imagens e gráficos gerados pela análise.

## 3. Tecnologias Utilizadas
* **PostgreSQL / SQL**: Para modelagem estruturada de dados, Constraints lógicas e consultas analíticas.
* **Python (Pandas)**: Limpeza de dados, casting de colunas, tratamento de nulos e lógica ETL.
* **Matplotlib e Seaborn**: Visualização de Dados.
* **Git e GitHub**: Versionamento de código (Padrão de commits: *Conventional Commits*).

## 4. Como Executar
1. Instale as dependências executando: `pip install -r requirements.txt`
2. Faça o download da base no Kaggle e insira em `data/raw/supermarket_sales.csv`.
3. Execute o script de banco em seu SGBD (pgAdmin, DBeaver) abrindo os arquivos `sql/01_criar_banco.sql` e `sql/02_criar_tabelas.sql`.
4. Rode a leitura inicial: `python src/01_leitura_dados.py`
5. Rode a transformação ETL: `python src/02_etl_vendas.py`
6. Rode as análises e gráficos: `python src/03_estatistica.py`

## 5. Resultados de Negócio Obtidos
Os scripts geram automaticamente as respostas para:
* A filial com maior faturamento e volume de vendas.
* O desempenho por linha de produto (financeiro e avaliação dos clientes).
* O ticket médio, valor máximo, dia de maior movimento e meio de pagamento favorito.
* Gráficos comprobatórios podem ser encontrados na pasta `/resultados`.
