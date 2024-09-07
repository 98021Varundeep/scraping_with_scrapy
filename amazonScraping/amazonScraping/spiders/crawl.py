import scrapy


class CrawlSpider(scrapy.Spider):
    name = "crawl"
    allowed_domains = ["scrapReviews"]
    start_urls = ["https://scrapReviews"]

    def parse(self, response):
        pass
