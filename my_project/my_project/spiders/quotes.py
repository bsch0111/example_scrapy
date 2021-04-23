""" http://quotes.toscrape.com/ 크롤러
메인 페이지만 크롤링해서 격언을 수집합니다.
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from my_project.items import Quote
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule

class QuotesSpider(CrawlSpider):
    """ Quote 아이템을 수집하는 크롤러"""
    
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response) :
        """ 크롤링한 페이지에서 Item을 스크레이핑합니다."""
        items = []
        for quote_html in response.css('div.quote'):
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            items.append(item)
        return item
        return items


    # def parse_item(self, response):
    #     item = {}
    #     #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item['name'] = response.xpath('//div[@id="name"]').get()
    #     #item['description'] = response.xpath('//div[@id="description"]').get()
    #     return item
