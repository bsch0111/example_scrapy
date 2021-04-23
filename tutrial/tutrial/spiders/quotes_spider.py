import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls= [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'qoutes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')