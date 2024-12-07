import pandas as pd
import numpy as np
import requests
import zipfile
import io
import xlsxwriter
import re
import time
import os 

output_directory = "./output/demonstrativos_raw"
os.makedirs(output_directory, exist_ok=True)


class load:

    def limpar_cnpj(self,cnpj):
    # Remover tudo que não seja número
        return re.sub(r'\D', '', str(cnpj))

    def load_data(self, link, cnpjs: list,  ticker: list, demonstrativos: list):
        list_of_list = []
        start_load = time.time()

        for index, cnpj in enumerate(cnpjs):
            start_enterprise = time.time()
            list_df = []

            for type_file in demonstrativos:
                arquivo_zip = requests.get(link)
                zf = zipfile.ZipFile(io.BytesIO(arquivo_zip.content))

                arquivo = f'itr_cia_aberta_{type_file}_con_2024.csv'
                file = zf.open(arquivo)

                lines = file.readlines()
                lines_decoed = [i.strip().decode('ISO-8859-1') for i in lines]
                lines_splited = [i.split(';') for i in lines_decoed]

                dataframe = pd.DataFrame(lines_splited[1:], columns = lines_splited[0])

                dataframe['CNPJ_CIA_AJUSTADO'] = dataframe['CNPJ_CIA'].apply(lambda x: self.limpar_cnpj(x))
                dataframe['VL_AJUSTADO'] = pd.to_numeric(dataframe['VL_CONTA'])

                filter_enterprise = dataframe[dataframe['CNPJ_CIA_AJUSTADO']==str(cnpj).zfill(6)]
                list_df.append(filter_enterprise)
                
                print(f'Trabalhando na empresa {str(ticker[index])}, no demonstrativo {type_file}. As dimensões são {filter_enterprise.shape}')

            list_of_list.append(list_df)

            output_path = os.path.join(output_directory, f'Demonstrativos_Empresa_{str(ticker[index])}.xlsx')
            writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

            for index_ , sheet_name in enumerate(demonstrativos):
            
                list_of_list[index][index_].to_excel(writer, sheet_name=f'{sheet_name}')

            print(f'Arquivo da empresa {str(ticker[index])} exportado')
            print('Tempo de execução de carregamento dessa empresa:', (time.time() - start_enterprise),'\n')

            writer.close()

        print('\n Tempo de execução', (time.time() - start_load))