import scrapy
import pandas as pd

class qualityLife(scrapy.Spider):
    name = 'cost'
    start_urls = [
        'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023-mid'   
    ]
    
    # response.xpath('//*[@id="t2"]/thead/tr/th//div/text()').getall()
    # data = response.xpath('//*[@id="t2"]/tbody/tr/td/text()').getall()
    def parse(self, response):
        header = response.xpath('//*[@id="t2"]/thead/tr/th//div/text()').getall()
        df = pd.DataFrame(columns = header)        
        rows = response.xpath('//*[@id="t2"]/tbody/tr')
        
        for row in rows:
            # Obtén los datos de cada fila como una lista
            row_data = row.xpath('./td/text()').getall()
            # Agrega la lista de datos al DataFrame como una nueva fila
            df.loc[len(df)] = row_data

        # Ahora df contiene la tabla completa
        df.to_csv('cost.csv', index = False)