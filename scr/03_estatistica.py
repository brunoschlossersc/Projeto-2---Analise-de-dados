import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analisar_dados():
    caminho_processed = os.path.join('data', 'processed', 'vendas_tratadas.csv')
    df = pd.read_csv(caminho_processed)
    
    # Converter data_venda de volta para datetime para facilitar extração do dia da semana
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    
    print("=== RESPOSTAS DE NEGÓCIO ===")
    
    # 1. Qual filial apresentou o maior faturamento?
    faturamento_filial = df.groupby('filial')['valor_total'].sum()
    print(f"1. Maior faturamento: Filial {faturamento_filial.idxmax()} (R$ {faturamento_filial.max():.2f})")
    
    # 2. Qual filial realizou a maior quantidade de vendas?
    qtd_filial = df['filial'].value_counts()
    print(f"2. Maior quantidade de vendas: Filial {qtd_filial.idxmax()} ({qtd_filial.max()} vendas)")
    
    # 3. Qual linha de produto apresentou o maior faturamento?
    fat_produto = df.groupby('linha_produto')['valor_total'].sum()
    print(f"3. Linha de produto c/ maior faturamento: {fat_produto.idxmax()} (R$ {fat_produto.max():.2f})")
    
    # 4. Qual linha de produto recebeu a melhor avaliação média?
    ava_produto = df.groupby('linha_produto')['avaliacao'].mean()
    print(f"4. Melhor avaliação média: {ava_produto.idxmax()} (Nota {ava_produto.max():.2f})")
    
    # 5. Qual foi a forma de pagamento mais utilizada?
    pagamento = df['forma_pagamento'].value_counts()
    print(f"5. Pagamento mais utilizado: {pagamento.idxmax()} ({pagamento.max()} vezes)")
    
    # 6. Qual foi o valor médio das vendas?
    valor_medio = df['valor_total'].mean()
    print(f"6. Valor médio das vendas: R$ {valor_medio:.2f}")
    
    # 7. Qual foi a maior venda registrada?
    maior_venda = df['valor_total'].max()
    print(f"7. Maior venda registrada: R$ {maior_venda:.2f}")
    
    # 8. Em qual dia da semana ocorreu a maior quantidade de vendas?
    df['dia_semana'] = df['data_venda'].dt.day_name()
    dia_mais_vendas = df['dia_semana'].value_counts()
    print(f"8. Dia com mais vendas: {dia_mais_vendas.idxmax()} ({dia_mais_vendas.max()} vendas)")

    # === GERAÇÃO DE GRÁFICOS ===
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
        
    plt.figure(figsize=(10,6))
    sns.barplot(x=faturamento_filial.index, y=faturamento_filial.values, palette='viridis')
    plt.title('Faturamento por Filial')
    plt.ylabel('Faturamento')
    plt.xlabel('Filial')
    plt.savefig('resultados/faturamento_filial.png')
    plt.close()

    plt.figure(figsize=(10,6))
    sns.barplot(y=fat_produto.index, x=fat_produto.values, palette='magma')
    plt.title('Faturamento por Linha de Produto')
    plt.xlabel('Faturamento')
    plt.ylabel('Linha de Produto')
    plt.savefig('resultados/faturamento_produto.png')
    plt.close()
    
    print("\nGráficos exportados com sucesso para a pasta 'resultados/'")

if __name__ == "__main__":
    analisar_dados()