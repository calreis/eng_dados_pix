PIPELINE DE DADOS EXTRAIDOS DA API BRASILAPI SOBRE O NÚMERO DE BANCOS PARTICIPANTES DO PIX E SUAS TRANSAÇÕES

OBS: 
Os dados são obtidos diretamente do Banco Central do Brasil.
Em novembro de 2025 o banco central deixou de fornecer a data de início de operação dos participantes, por isso este campo pode estar vazio para alguns participantes.

GRÁFICO SIMPLES GERADO COM GRAFANA 
<img width="1920" height="1080" alt="grafico_grafana" src="https://github.com/user-attachments/assets/93411822-d6b4-4da4-9a6f-19eb23f27c43" />
gráfico sobre o número de participantes do SPI(Sistema de pagamentos instâtaneos)

ESTRUTURA DAS PASTAS
eng_dados/
├── scripts/               # Códigos Python
│   ├── coleta.py          # Script de Extração (API -> CSV)
│   └── carga.py           # Script de Carga (CSV -> Postgres)
├── deploy/                # Arquivos de infraestrutura
│   └── docker-compose.yml # Configuração do Postgres e Grafana
├── data/                  # (Opcional) Apenas para exemplos pequenos
│   └── .gitkeep           # Evita subir CSVs gigantes, mas mantém a pasta
├── README.md              # Documentação do projeto
└── .gitignore             # Arquivos que o Git deve ignorar (venv, pycache)
