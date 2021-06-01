import argparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from url_extractor.spiders.urls import UrlsSpider


my_parser = argparse.ArgumentParser(description='providing the domain and file where you store urls')

my_parser.add_argument('-t',
                       type=str,
                       help='the domain that you need to scrape the url from')

my_parser.add_argument('-o',
                       type=str,
                       help='the path to list')

args = my_parser.parse_args()

if __name__ == '__main__':
    settings = get_project_settings()
    settings['FEED_URI'] = args.o
    process = CrawlerProcess(settings=settings)
    process.crawl(UrlsSpider,domain=args.t)
    process.start()