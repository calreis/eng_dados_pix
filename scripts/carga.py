import pandas as pd
from sqlalchemy import create_engine, text

# Conexão
engine = create_engine('postgresql://usuario_eng:senha_forte@localhost:5432/dw_pix')

def carga_final():
    # 1. Carregar CSV
    df = pd.read_csv("participantes_pix_raw.csv")
    print(f"Total no CSV: {len(df)} linhas.")

    # 2. TRATAMENTO DE DATA (O Ponto Crítico)
    # Se a API mandou vazio, vamos preencher com uma data padrão para não perder a linha
    # ou simplesmente não deletar tudo se falhar.
    df['inicio_operacao'] = pd.to_datetime(df['inicio_operacao'], errors='coerce')
    
    # Em vez de dropar tudo que deu erro, vamos ver quantas datas falharam
    erros_data = df['inicio_operacao'].isna().sum()
    print(f"Atenção: {erros_data} linhas com data inválida.")

    # 3. SQL Nativo para Dropar a View (Correção para SQLAlchemy 2.0)
    with engine.begin() as conn:
        # No SQLAlchemy 2.0, strings SQL precisam da função text()
        conn.execute(text("DROP VIEW IF EXISTS vw_analise_adesao_pix CASCADE;"))
    
    # 4. Enviar para o Postgres
    df.to_sql('fato_participantes_pix', con=engine, if_exists='replace', index=False)
    print("✓ Dados carregados no Postgres!")

if __name__ == "__main__":
    carga_final()
