from openpyxl import Workbook


class RelatorioExcel:
    @staticmethod
    def gerar_relatorio(caminho_arquivo, tickers):
        wb = Workbook()
        ws = wb.active
        ws.title = "Indicadores"
        ws.append(["Ticker", "Indicador", "Valor"])
        for ticker in tickers:
            for indicador, valor in ticker.indicators.items():
                ws.append([ticker.symbol, indicador, valor])
            ws.append([ticker.symbol, "Balanço", ticker.balanco])
        wb.save(caminho_arquivo)
