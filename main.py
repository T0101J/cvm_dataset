# from indicators_calc import GerenciadorTickers
from relatorio_excel import RelatorioExcel
from get_data import load 
from make_table import Table
import pandas as pd

# Configuração de diretórios
DIRETORIO_GRAFICOS = "./graficos"
ARQUIVO_RELATORIO = "./output/indicadores.xlsx"


ANO_REFERENCIA = 2024
FONTE_DADOS = f"http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_{ANO_REFERENCIA}.zip"
FONTE_BALANCO = "fonte_balanco"
DEMOSTRATIVOS = ['DFC_MI','BPA','DRE','BPP']
# DFC_MD - Demonstração de Fluxo de Caixa - Método Direto
# DFC_MI - Demonstração de Fluxo de Caixa - Método Indireto
# BPA - Demonstração de Patrimonial Ativo
# BPP - Demonstração de Patrimonial Ativo
# DRE - Demonstração de Resultado

ticker = pd.read_excel('./input/TICKERS.xlsx')
tickers = ticker['Tickers']
cnpjs = list(ticker['cnpj'])

# # Carregando dados
get_data = load()
get_data.load_data(FONTE_DADOS, cnpjs, tickers,DEMOSTRATIVOS)
# Formata as tabelas
make_table = Table(tickers,DEMOSTRATIVOS)

# Gerando indicadores

# Gerando gráfico
print("Processo concluído.")
