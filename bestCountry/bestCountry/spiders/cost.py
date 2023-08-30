import scrapy

class qualityLife(scrapy.Spider):
    name = 'cost'
    start_urls = [
        'https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2023-mid'   
    ]
    
    
    # Extract data
    def parse(self, response):
        
        table_data = {}

        # Determine the number of columns dynamically
        num_columns = len(response.xpath('//*[@id="t2"]/thead/tr/th').extract())

        for i in range(num_columns):
            header = response.xpath(f'//*[@id="t2"]/thead/tr/th[{i + 1}]//div/text()').get()
            column_data = []
            j = 0
            while True:
                j += 1
                rows = response.xpath(f'//*[@id="t2"]/tbody/tr[{j}]/td[{i+1}]/text()').getall()
                if not rows:
                    break
                column_data.append(rows)
            table_data[header] = column_data

        print(table_data)