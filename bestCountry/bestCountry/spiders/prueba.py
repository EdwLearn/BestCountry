import os
import pandas as pd
import scrapy

class qualityLife(scrapy.Spider):
    name = 'prueba'
    start_urls = [
        'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023-mid'
    ]

    def parse(self, response):
        # Obtén los valores de los años
        years = response.xpath("//form[@class='changePageForm']/select[@name='title']/option/@value").getall()
        for year_value in years:
            # Construye la URL completa
            url = f"https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title={year_value}"

            # Utiliza response.follow para seguir la URL y pasa year_value como argumento
            yield response.follow(url, callback=self.parse_table, cb_kwargs={'year_value': year_value})

    def parse_table(self, response, year_value):
        # Extrae la tabla de datos de la página vinculada
        header = response.xpath('//*[@id="t2"]/thead/tr/th//div/text()').getall()
        df = pd.DataFrame(columns=header)
        rows = response.xpath('//*[@id="t2"]/tbody/tr')

        for row in rows:
            row_data = row.xpath('./td/text()').getall()
            df.loc[len(df)] = row_data

        # Guarda el DataFrame en un archivo CSV con el nombre del enlace
        data_folder = 'data'

        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        # Guarda el DataFrame en un archivo CSV dentro de la carpeta "data" con el nombre del enlace
        df.to_csv(os.path.join(data_folder, f'cost-{year_value}.csv'), index=False)

        # Puedes imprimir el nombre del archivo generado si lo deseas
        # self.logger.info(f'Guardado: cost-{year_value}.csv')


""" import os
import pandas as pd
import scrapy


    # response.xpath('//form[@method="get"]/select[@name="title"]/option/@value').extract() extraer nombres de links

class qualityLife(scrapy.Spider):
    name = 'prueba'
    start_urls = [
        'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023-mid'   
    ]
    
    def __init__(self):
        super().__init__()
        self.year_value = None

    def parse(self, response):
            
        # Obtén los valores de los años
        years = response.xpath("//form[@class='changePageForm']/select[@name='title']/option/@value").getall()
        for year_value in years:
        # Construye la URL completa
            url = f"https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title={year_value}"
            
            
            self.year_value = year_value
            
            
        # Utiliza response.follow para seguir la URL
            yield response.follow(url, callback=self.parse_table)

    def parse_table(self, response):
        # Extrae la tabla de datos de la página vinculada
        header = response.xpath('//*[@id="t2"]/thead/tr/th//div/text()').getall()
        df = pd.DataFrame(columns=header)
        rows = response.xpath('//*[@id="t2"]/tbody/tr')

        for row in rows:
            row_data = row.xpath('./td/text()').getall()
            df.loc[len(df)] = row_data
        print('save df')
            
        # Extrae el nombre del enlace para usarlo como nombre de archivo
        year_value = self.year_value
        
        # Guarda el DataFrame en un archivo CSV con el nombre del enlace 
        #data_folder = 'data'
        
        #if not os.path.exists(data_folder):
            #os.makedirs(data_folder)
        
        # Guarda el DataFrame en un archivo CSV dentro de la carpeta "data" con el nombre del enlace
        # for year in year_value:
            #df.to_csv(os.path.join(data_folder, f'cost-{year}.csv'), index=False)
        print(f'save {year_value}')

        # Puedes imprimir el nombre del archivo generado si lo deseas
        # self.logger.info(f'Guardado: cost-{link_name}.csv')"""