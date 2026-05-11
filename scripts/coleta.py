import requests
import pandas as pd
from datetime import datetime
import os

def buscar_dados_pix():
    url = "https://brasilapi.com.br"
    headers = {"User-Agent": "Mozilla/5.0"}
    print(f"[{datetime.now()}] Iniciando extração de dados do PIX...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        dados = response.json()
        print(f"✓ Sucesso! {len(dados)} instituições encontradas.")
        return dados
    except Exception as e:
        print(f"X Erro ao acessar a API: {e}")
        return None

def transformar_e_salvar(dados):
    if not dados:
        return
    
    df = pd.DataFrame(dados)
    df['inicio_operacao'] = pd.to_datetime(df['inicio_operacao'], errors='coerce')
    df['data_carga'] = datetime.now()
    
    # --- CORREÇÃO DO CAMINHO AQUI ---
    # Pega a pasta onde este script está (scripts/), sobe uma (..) e entra em data/
    base_path = os.path.dirname(os.path.abspath(__file__))
    nome_arquivo = os.path.join(base_path, "..", "data", "participantes_pix_raw.csv")
    
    # Verifica se a pasta data existe, se não, cria ela
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)
    
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    print(f"✓ Dados salvos com sucesso em: {nome_arquivo}")

if __name__ == "__main__":
    lista_pix = buscar_dados_pix()
    transformar_e_salvar(lista_pix)
