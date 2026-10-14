import pandas as pd
import os

def ler_e_inspecionar():
    caminho_arquivo = os.path.join('data', 'raw', 'supermarket_sales.csv')
    
    print(f"Lendo arquivo bruto em: {caminho_arquivo}")
    df = pd.read_csv(caminho_arquivo)
    
    print("\n--- Visualização Inicial (Head) ---")
    print(df.head())
    
    print("\n--- Informações do DataFrame ---")
    df.info()
    
    print("\n--- Verificação de Valores Nulos ---")
    print(df.isnull().sum())
    
    print("\n--- Estatísticas Descritivas Básicas ---")
    print(df.describe(include='all'))
    
    return df

if __name__ == "__main__":
    df_raw = ler_e_inspecionar()