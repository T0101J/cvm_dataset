# Projeto de Análise de Dados de Empresas

Este projeto tem como objetivo processar dados financeiros de empresas, organizando-os em tabelas que podem ser usadas para análises. O fluxo do projeto envolve a extração de dados a partir de uma planilha de entrada, a transformação dos dados e a organização final dos dados em diferentes formatos.

## Estrutura de Pastas

### 1. `input/`
Contém a planilha de entrada, onde você deve colocar os Tickers e CNPJs das empresas a serem analisadas. A planilha deve ter as colunas:
- **Ticker**: O código da ação da empresa.
- **CNPJ**: O número do CNPJ da empresa.

### 2. `output/`
A pasta `output/` contém as pastas de resultado do processamento dos dados.

- **raw/**: Nesta pasta, você encontrará os dados crus extraídos. Estes dados são os resultados iniciais obtidos do site da CVM (ou outro local de origem).
  
- **bronze/**: Contém as tabelas transformadas e organizadas por empresa. Após a extração dos dados, a pasta bronze organiza os demonstrativos financeiros em um formato mais estruturado.

### 3. Scripts
Os scripts do projeto são responsáveis por processar os dados da planilha de entrada e gerar os resultados. Eles são:

- **get_data.py**: Script para buscar os dados das empresas (utiliza o ticker e CNPJ como entrada).
- **graficos.py**: Gera gráficos baseados nos dados extraídos.
- **indicators_calc.py**: Calcula indicadores financeiros baseados nos dados extraídos.
- **make_table.py**: Organiza e cria as tabelas financeiras.
- **relatorio_excel.py**: Gera relatórios em Excel.
- **main.py**: O script principal que orquestra a execução de todos os outros scripts.

### 4. Arquivos de Configuração

- **requirements.txt**: Contém as dependências necessárias para rodar o projeto. Utilize este arquivo para instalar as bibliotecas necessárias usando o comando:
  
  ```bash
  pip install -r requirements.txt


## Como Usar

### 1. Preparação dos Dados
   - Coloque os dados de entrada na pasta `input/`, no formato de uma planilha. A planilha deve conter as seguintes colunas:
     - **Ticker**: O código da ação da empresa.
     - **CNPJ**: O número do CNPJ da empresa.
   
### 2. Executando o Script
   - Para rodar o processamento completo, execute o script principal `main.py`. Este script irá buscar os dados de acordo com os Tickers e CNPJs fornecidos e processá-los conforme as etapas definidas no projeto.
   
   Execute o seguinte comando no terminal:
   
   ```bash
   python main.py


### 3. Acessando os Resultados

Após o processamento, você encontrará os resultados nas pastas dentro da pasta `output/`:

- **raw/**: Contém os dados crus extraídos, sem nenhuma transformação.
- **bronze/**: Contém os dados organizados por empresa, com tabelas transformadas e ajustadas para análise.

As pastas dentro de `output/` são estruturadas da seguinte maneira:

- **raw/**: Dados extraídos diretamente sem alterações.
- **bronze/**: Tabelas organizadas, com os dados ajustados para cada empresa.

Você pode acessar essas pastas para visualizar os dados processados em seus respectivos formatos.

