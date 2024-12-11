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

        demonstrativos.remove('BPP')

        files_found = [f for f in arquivos if f.endswith('xlsx')]
        os.makedirs(output_directory_bronze, exist_ok=True)

        for ticker in tickers:
            tk = time.time()

            caminho_saida = os.path.join(output_directory_bronze, f"Demonstrativos_Empresa_{ticker}.xlsx")
            writer = pd.ExcelWriter(caminho_saida, engine='xlsxwriter')

            for document in demonstrativos:

                sheet_df = self.document_handler(ticker, files_found, document)        
                sheet_df.to_excel(writer, sheet_name=f'{document}')
            
            writer.close()
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

        if document == 'BPA':
            # Combinar BPA e BPP
            other_document = 'BPA' if document == 'BPP' else 'BPP'
            df_other_list = []

            for f in arquivos_xls:
                if ticker in f:
                    caminho_arquivo = os.path.join(output_directory_raw, f)
                    xls_other = pd.read_excel(caminho_arquivo, sheet_name=f'{other_document}')
                    xls_other['TICKER'] = ticker
                    df_other_list.append(xls_other)

            df_other = pd.concat(df_other_list, ignore_index=True)

            df['TIPO'] = 'Ativo'
            df_other['TIPO'] = 'Passivo'

            df = pd.concat([df, df_other], ignore_index=True)

            # Pivot table
            df = pd.pivot_table(
                df,
                index=['DENOM_CIA', 'TICKER', 'TIPO', 'CD_CONTA', 'DS_CONTA'],
                columns=['DT_REFER', 'DT_FIM_EXERC'],
                values=['VL_AJUSTADO']
            )

            sheet_name = 'BP'
        else:
            if document == 'DRE':
                df = pd.pivot_table(
                    df,
                    index=['DENOM_CIA', 'TICKER', 'CD_CONTA', 'DS_CONTA'],
                    columns=['DT_INI_EXERC', 'DT_FIM_EXERC'],
                    values=['VL_AJUSTADO']
                )
            else:
                df = pd.pivot_table(
                    df,
                    index=['DENOM_CIA', 'TICKER', 'CD_CONTA', 'DS_CONTA'],
                    columns=['DT_REFER', 'DT_FIM_EXERC'],
                    values=['VL_AJUSTADO']
                )
            sheet_name = document

        print(f'\n Tempo de execução da transformação {sheet_name} da empresa {ticker}', (time.time() - start))

        return df