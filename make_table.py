import pandas as pd
import os
import time
import xlsxwriter

output_directory_raw = "./output/demonstrativos_raw"
output_directory_bronze = "./output/demonstrativos_bronze"
output_directory_silver = "./output/demonstrativos_silver"
output_directory_gold = "./output/demonstrativos_gold"

arquivos = os.listdir(output_directory_raw)

# bpp = DT_REFER','DT_FIM_EXERC
# bpa =DT_REFER','DT_FIM_EXERC
# dre = 'DT_INI_EXERC', 'DT_FIM_EXERC
# dfcDT_REFER','DT_FIM_EXERC

class Table:
    def __init__(self, tickers,demonstrativos):

        files_found = [f for f in arquivos if f.endswith('xlsx')]
        os.makedirs(output_directory_bronze, exist_ok=True)

        for ticker in tickers:
            tk = time.time()

            for document in demonstrativos:

                self.document_handler(ticker, files_found, document)

            print(f'Excel da {ticker} criado em {time.time() - tk} segundos!')

    def document_handler(self, ticker, arquivos_xls, document):
        start = time.time()
        df_list = [] 

        for f in arquivos_xls:
            if ticker in f:
                caminho_arquivo = os.path.join(output_directory_raw, f) 
                xls = pd.read_excel(caminho_arquivo, sheet_name=f'{document}')
                xls['TICKER'] = ticker
                df_list.append(xls) 

        df = pd.concat(df_list, ignore_index=True)
        if document == 'DRE':
            df = pd.pivot_table(df,
                                index=['DENOM_CIA','TICKER','CD_CONTA','DS_CONTA'],
                                columns=['DT_INI_EXERC', 'DT_FIM_EXERC'],
                                values=['VL_AJUSTADO'])
        else:
            df = pd.pivot_table(df,
                                index=['DENOM_CIA','TICKER','CD_CONTA','DS_CONTA'],
                                columns=['DT_REFER', 'DT_FIM_EXERC'],
                                values=['VL_AJUSTADO'])

        caminho_saida = os.path.join(output_directory_bronze, f"Demonstrativos_Empresa_{ticker}.xlsx")
        
        writer = pd.ExcelWriter(caminho_saida, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=f'{document}')
        writer.close()
        print(f'\n Tempo de execução da transformação {document} da empresa {ticker}', (time.time() - start))
