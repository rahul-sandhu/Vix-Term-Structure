import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import date


class VixSpider(scrapy.Spider):
    name = "VixSpider"

    start_urls = [
        "http://vixcentral.com/historical/?days=21"
    ]

    def parse(self, response):

        for i in range(len(response.css('td::text').re(r'\d\d\d\d[-]\d\d[-]\d\d'))):
            yield {
                'date': response.css('td::text')[17+(i*17)].get(),
                'first_month': response.css('td::text')[18+(i*17)].get(),
                'F1': response.css('td::text')[19+(i*17)].get(),
                'F2': response.css('td::text')[20+(i*17)].get(),
                'F3': response.css('td::text')[21+(i*17)].get(),
                'F4': response.css('td::text')[22+(i*17)].get(),
                'F5': response.css('td::text')[23+(i*17)].get(),
                'F6': response.css('td::text')[24+(i*17)].get(),
                'F7': response.css('td::text')[25+(i*17)].get(),
                'F8': response.css('td::text')[26+(i*17)].get(),
                'F9': response.css('td::text')[27+(i*17)].get(),
            }


# today = date.today()
# date = today.strftime("%m.%d.%y")

# process = CrawlerProcess(settings={
#     'FEED_FORMAT': 'json',
#     'FEED_URI': 'VIX.json'})


# process.crawl(VixSpider)
# process.start(stop_after_crawl=False)
