import requests
import pandas as pd
from datetime import datetime

def buscar_dados_pix():
    url = "https://brasilapi.com.br/api/pix/v1/participants"
    
    print(f"[{datetime.now()}] Iniciando extração de dados do PIX...")
    
    try:
        response = requests.get(url)
        # Verifica se a requisição deu certo (Status 200)
        response.raise_for_status() 
        
        dados = response.json()
        print(f"✓ Sucesso! {len(dados)} instituições encontradas.")
        return dados
    
    except requests.exceptions.RequestException as e:
        print(f"X Erro ao acessar a API: {e}")
        return None

def transformar_e_salvar(dados):
    if not dados:
        return
    
    # Converte JSON para DataFrame (Tabela)
    df = pd.DataFrame(dados)
    
    # Pequena limpeza: Converter a coluna de data para o formato datetime do Python
    df['inicio_operacao'] = pd.to_datetime(df['inicio_operacao'])
    
    # Criar uma coluna simples de auditoria: "data_da_carga"
    df['data_carga'] = datetime.now()
    
    # Salva em CSV para você visualizar o resultado imediatamente
    nome_arquivo = "participantes_pix_raw.csv"
    df.to_csv(nome_arquivo, index=False, encoding='utf-8')
    
    print(f"✓ Dados salvos com sucesso em: {nome_arquivo}")
    print("\nVisualização das primeiras linhas:")
    print(df.head(3))

if __name__ == "__main__":
    lista_pix = buscar_dados_pix()
    transformar_e_salvar(lista_pix)
