# Pipeline de Dados: Participantes do PIX 🚀

Este projeto é um pipeline de dados automatizado que extrai, transforma e carrega (ETL) informações públicas sobre as instituições participantes do PIX, utilizando a API pública do BrasilAPI.

## 📊 Resultados obtidos

- Dados atualizados diariamente com informações do dia atual ou último dia útil
- Processo 100% automatizado, sem intervenção manual
- Redução de 100% no tempo de coleta vs. processo manual
- Dashboard no Grafana para consulta e filtros por data e tipo de instituição

## 🛠️ Estrutura do Projeto

eng_dados_pix/
├── scripts/ # Automações Python para ETL
├── deploy/ # Docker + Docker Compose (Postgres + Grafana)
├── sql/ # Views e queries analíticas
├── data/ # Dados brutos extraídos (CSV temporário)
└── README.md # Documentação
