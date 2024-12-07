# Projeto de Extração e análise fundamentalista 
Este projeto tem como objetivo processar dados financeiros de empresas, organizando-os em tabelas que podem ser usadas para análises. O fluxo do projeto envolve a extração de dados a partir de uma planilha de entrada, a transformação dos dados e a organização final dos dados em diferentes formatos.

Estrutura de Pastas
1. input/
Contém a planilha de entrada, onde você deve colocar os Tickers e CNPJs das empresas a serem analisadas. A planilha deve ter as colunas:

Ticker: O código da ação da empresa.
CNPJ: O número do CNPJ da empresa.
2. output/
A pasta output/ contém as pastas de resultado do processamento dos dados.

raw/: Nesta pasta, você encontrará os dados crus extraídos. Estes dados são os resultados iniciais obtidos do site da CVM (ou outro local de origem).

bronze/: Contém as tabelas transformadas e organizadas por empresa. Após a extração dos dados, a pasta bronze organiza os demonstrativos financeiros em um formato mais estruturado.

3. Scripts
Os scripts do projeto são responsáveis por processar os dados da planilha de entrada e gerar os resultados. Eles são:

get_data.py: Script para buscar os dados das empresas (utiliza o ticker e CNPJ como entrada).
graficos.py: Gera gráficos baseados nos dados extraídos.
indicators_calc.py: Calcula indicadores financeiros baseados nos dados extraídos.
make_table.py: Organiza e cria as tabelas financeiras.
relatorio_excel.py: Gera relatórios em Excel.
main.py: O script principal que orquestra a execução de todos os outros scripts.
4. Arquivos de Configuração
requirements.txt: Contém as dependências necessárias para rodar o projeto. Utilize este arquivo para instalar as bibliotecas necessárias usando o comando:

bash
Copiar código
pip install -r requirements.txt
.gitignore: Arquivo para ignorar arquivos e pastas desnecessárias, como o ambiente virtual (cvm/) e arquivos temporários do Python (__pycache__/, *.pyc).

Como Usar
Preparação dos Dados:

Coloque os dados de entrada na pasta input/ em formato de planilha, com os Tickers e CNPJs das empresas que você deseja analisar.
Executando o Script:

Execute o script main.py para rodar o processamento completo.
bash
Copiar código
python main.py
Acessando os Resultados:

Após o processamento, os resultados estarão nas pastas output/raw/ (dados crus) e output/bronze/ (dados organizados por empresa).
Dependências
As dependências podem ser instaladas utilizando o arquivo requirements.txt. Execute o seguinte comando:

bash
Copiar código
pip install -r requirements.txt
Bibliotecas Necessárias:
pandas
xlsxwriter
numpy
requests
(Outras dependências conforme necessário)
