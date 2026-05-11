import pandas as pd
from sqlalchemy import create_engine, text
import os

engine = create_engine('postgresql://usuario_eng:senha_forte@localhost:5432/dw_pix')

def carga_final():
    # Detecta onde o script está e aponta para a pasta data na raiz do projeto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Se o script estiver na raiz, use 'data/...' 
    # Se estiver em scripts/, use '../data/...'
    # Vamos usar uma lógica que tenta ambos:
    caminhos_possiveis = [
        os.path.join(base_dir, "data", "participantes_pix_raw.csv"),
        os.path.join(base_dir, "..", "data", "participantes_pix_raw.csv")
    ]
    
    df = None
    for caminho in caminhos_possiveis:
        if os.path.exists(caminho):
            df = pd.read_csv(caminho)
            print(f"✓ Arquivo encontrado em: {caminho}")
            break
            
    if df is None:
        print("X Erro: Arquivo CSV não encontrado em nenhuma das pastas esperadas.")
        return

    # Processamento e Carga
    df['inicio_operacao'] = pd.to_datetime(df['inicio_operacao'], errors='coerce')
    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS vw_analise_adesao_pix CASCADE;"))
    
    df.to_sql('fato_participantes_pix', con=engine, if_exists='replace', index=False)
    print(f"✓ Sucesso! {len(df)} linhas carregadas.")

if __name__ == "__main__":
    carga_final()
