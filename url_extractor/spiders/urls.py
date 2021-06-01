import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from url_extractor.items import UrlExtractorItem


class UrlsSpider(CrawlSpider):
    name = 'urls'
    file= 'data.txt'
    def __init__(self,domain, *a, **kw):
        super(UrlsSpider, self).__init__(*a, **kw)
        self.start_urls = [
            'http://www.' + domain,
            'http://' + domain,
            ]
        self.allowed_domains = [
            domain
        ]


    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )




    def parse_item(self, response):
        loader = ItemLoader(UrlExtractorItem(),response)
        loader.add_value('url',response.url)
        yield loader.load_item()