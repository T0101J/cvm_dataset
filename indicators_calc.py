import os
import numpy as np
import pandas as pd

INDICADORES = [ 'Margem Bruta'
                ,'Margem Liquida'
                ,'Dívida Bruta/Patrimônio Líquido'
                ,'Disponibilidades'
                ,'Liquidez Corrente'
                ,'EBIT'
                ,'ebit_ajustado'
                ,'Margem operacional'
                ,'Ebitda/Divida Bruta'
                ,'ROE E ROIC'
                ,'EBIT/Ativo'
                ,'ROIC'
                ,'Equity e Preço'
                ,'Valor de Mercado'
                ,'Enterprise Value'
                ,'Valor Patrimonial da Ação'
                ,'LPA'
                ,'#P/L'
                ,'Dividendos'
                ,'Dividend Yield']

class Calculate:
    def __init__(self):

        pass

    def make_tables():

        pass

    def indicators_calc(self, fonte_dados, fonte_balanco, diretorio_graficos):
        for ticker in self.tickers:
            ticker.carregar_dados(fonte_dados)
            ticker.carregar_balanco(fonte_balanco)
            ticker.calcular_indicadores()
            ticker.gerar_graficos(diretorio_graficos)
