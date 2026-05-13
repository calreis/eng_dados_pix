
<h>Pipeline de Dados: Participantes do PIX 🚀</h>
  
</p>Este projeto é um pipeline de dados automatizado que extrai, transforma e carrega (ETL) informações públicas sobre as instituições participantes do PIX, utilizando a API pública do BrasilAPI.</p>

<h2>🛠️ Estrutura do ProjetoO repositório está organizado da seguinte forma:scripts/:</h2>

<p>O repositório está organizado da seguinte forma:scripts/: Automações em Python para o processo de ETL.deploy/: Infraestrutura via Docker para o banco de dados Postgres e painéis no Grafana.sql/: Camada de transformação de dados contendo as Views e Queries analíticas.data/: Armazenamento temporário dos arquivos brutos extraídos (CSV).README.md: Documentação oficial do projeto.</p>

<img width="651" height="199" alt="estrutuda" src="https://github.com/user-attachments/assets/582f1587-4c42-4200-8727-ad946f3899f3" />

<h2>🏗️ Como Funciona o Pipeline (ETL)<h2>

<p>1. Extração e Transformação Inicial (scripts/) O script consome os dados de participantes do PIX a partir do endpoint da BrasilAPI.Converte a resposta JSON em um DataFrame do Pandas.Normaliza os campos de data (inicio_operacao).Cria uma coluna de auditoria chamada data_carga.Salva os resultados iniciais no arquivo temporário data/participantes_pix_raw.csv.</p>

<p>2. Carga dos Dados (Data Warehouse) O script de carga final lê o arquivo CSV gerado.Conecta-se ao banco de dados PostgreSQL rodando via Docker.Remove views legadas para evitar conflitos de esquema.Insere ou substitui os dados atualizados na tabela de destino fato_participantes_pix.</p>

<h2>🚀 Como Executar o Projeto</h2>
<h3>Pré-requisitos</h3>
<p>* Python 3.8 ou superior instalado.</p>
<p>* Docker e Docker Compose configurados.</p>

<h2>Passo 1: Subir a Infraestrutura</h2>
<p>Navegue até a pasta de deploy e inicie os serviços do banco de dados e monitoramento:</p>
<img width="638" height="103" alt="Captura de tela 2026-05-13 084737" src="https://github.com/user-attachments/assets/e97299fc-a4a6-49bc-9010-8f0b2d054963" />

<h2>Passo 2: Instalar as Dependências do Python</h2>

<p>Instale as bibliotecas necessárias para rodar os scripts de ETL:</p>

<img width="472" height="137" alt="image" src="https://github.com/user-attachments/assets/f247c399-6f9a-4d1e-89e4-f04946a9d3f5" />

<h2>Passo 3: Executar a Extração de Dados<h2>
  
<p>Execute o script responsável por buscar as informações diretamente na API:</p>
<img width="644" height="82" alt="image" src="https://github.com/user-attachments/assets/a3660822-07ef-4ace-8333-3b7c1615b585" />

<h2>Passo 4: Executar a Carga no Banco de Dados</h2>

<p>Execute o script que envia os dados tratados para o Data Warehouse no Postgres:</p>

<img width="509" height="85" alt="image" src="https://github.com/user-attachments/assets/39816eeb-d4c7-4b99-a39c-faaf744a57fa" />

📊 Visualização e AnáliseOs dados carregados na tabela fato_participantes_pix ficam disponíveis para consultas SQL personalizadas na pasta data/.Você pode conectar o seu painel do Grafana (disponibilizado via Docker) ao banco Postgres para criar gráficos sobre a evolução e adesão das instituições ao PIX ao longo do tempo.

<img width="1920" height="1080" alt="grafico_grafana" src="https://github.com/user-attachments/assets/93411822-d6b4-4da4-9a6f-19eb23f27c43" />
<p>gráfico sobre o número de participantes do SPI(Sistema de pagamentos instâtaneos)</p>




