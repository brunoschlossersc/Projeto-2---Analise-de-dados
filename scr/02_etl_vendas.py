import pandas as pd
import os

def executar_etl():
    caminho_raw = os.path.join('data', 'raw', 'supermarket_sales.csv')
    df = pd.read_csv(caminho_raw)

    # 1. Padronização do nome das colunas para o dicionário solicitado
    df = df.rename(columns={
        'Invoice ID': 'id_venda',
        'Branch': 'filial',
        'City': 'cidade',
        'Customer type': 'tipo_cliente',
        'Gender': 'genero',
        'Product line': 'linha_produto',
        'Unit price': 'preco_unitario',
        'Quantity': 'quantidade',
        'Tax 5%': 'imposto',
        'Total': 'valor_total',
        'Date': 'data_venda',
        'Time': 'hora_venda',
        'Payment': 'forma_pagamento',
        'cogs': 'custo_mercadoria',
        'gross margin percentage': 'margem_percentual',
        'gross income': 'receita_bruta',
        'Rating': 'avaliacao'
    })

    # 2. Tipagem Correta (Casting) e tratamento de datas
    df['data_venda'] = pd.to_datetime(df['data_venda']).dt.date
    # 'hora_venda' já vem num formato HH:MM, podemos manter como string ou datetime.time
    df['hora_venda'] = pd.to_datetime(df['hora_venda'], format='%H:%M').dt.time

    colunas_numericas = ['preco_unitario', 'imposto', 'valor_total', 
                         'custo_mercadoria', 'margem_percentual', 'receita_bruta', 'avaliacao']
    df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')
    df['quantidade'] = df['quantidade'].astype(int)

    # 3. Tratamento de Nulos e Duplicatas
    df = df.drop_duplicates()
    df = df.dropna(subset=['id_venda', 'filial', 'cidade', 'linha_produto']) # Remove essenciais nulos
    
    # 4. Coluna Derivada / Conferência de Integridade
    # Verifica se preco * qtd + imposto bate com o valor_total (margem de erro de 0.01 por arredondamento)
    df['valor_total_calculado'] = (df['preco_unitario'] * df['quantidade']) + df['imposto']
    df['diferenca_calculo'] = abs(df['valor_total'] - df['valor_total_calculado'])
    # Você pode dropar essas colunas auxiliares se desejar manter só o modelo final
    df = df.drop(columns=['valor_total_calculado', 'diferenca_calculo'])

    # 5. Exportar Base Tratada
    caminho_processed = os.path.join('data', 'processed', 'vendas_tratadas.csv')
    df.to_csv(caminho_processed, index=False)
    print(f"ETL concluído com sucesso. Arquivo salvo em: {caminho_processed}")

if __name__ == "__main__":
    executar_etl()