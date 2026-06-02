# Pipeline de Dados: Participantes do PIX 🚀

Este projeto é um pipeline de dados automatizado que extrai, transforma e carrega (ETL) informações públicas sobre as instituições participantes do PIX, utilizando a API pública do BrasilAPI.

## 📊 Resultados obtidos

- Dados atualizados diariamente com informações do dia atual ou último dia útil
- Processo 100% automatizado, sem intervenção manual
- Redução de 100% no tempo de coleta vs. processo manual
- Dashboard no Grafana para consulta e filtros por data e tipo de instituição

## 🛠️ Estrutura do Projeto

eng_dados_pix/
├── scripts/          # Automações Python para ETL
├── deploy/           # Docker + Docker Compose (Postgres + Grafana)
├── sql/              # Views e queries analíticas
├── data/             # Dados brutos extraídos (CSV temporário)
└── README.md         # Documentação

## 🏗️ Como Funciona o Pipeline (ETL)

### 1. Extração e Transformação (scripts/coleta.py)

- Consome a API da BrasilAPI (endpoint de participantes do PIX)
- Converte JSON para DataFrame Pandas
- Normaliza datas e adiciona coluna de auditoria (data_carga)
- Salva em data/participantes_pix_raw.csv

### 2. Carga no Data Warehouse (scripts/carga.py)

- Lê o CSV gerado
- Conecta ao PostgreSQL (rodando via Docker)
- Remove views legadas para evitar conflitos
- Insere/substitui dados na tabela fato_participantes_pix

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8+
- Docker e Docker Compose

### Passo 1: Subir a Infraestrutura

Navegue até a pasta deploy e inicie os containers:

cd deploy/
docker-compose up -d

### Passo 2: Instalar Dependências Python

pip install -r requirements.txt

### Passo 3: Executar a Extração de Dados

python scripts/coleta.py

### Passo 4: Executar a Carga no Banco

python scripts/carga.py

## 📈 Visualização e Análise

Os dados carregados na tabela fato_participantes_pix podem ser consultados via SQL ou conectados ao Grafana (disponível via Docker) para criar dashboards interativos.

Exemplo de query:

SELECT 
    data_carga,
    COUNT(*) as total_participantes
FROM fato_participantes_pix
GROUP BY data_carga
ORDER BY data_carga DESC;

### Dashboard no Grafana

Gráfico mostrando evolução do número de participantes do SPI (Sistema de Pagamentos Instantâneos)

## 🧠 Tecnologias utilizadas

- Python (Pandas, requests)
- PostgreSQL
- Docker & Docker Compose
- Grafana
- BrasilAPI

## 📬 Contato

Claudemir dos Reis – LinkedIn: linkedin.com/in/claudemir-dos-reis-da-silva-2577152b8
GitHub: github.com/calreis

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório!
