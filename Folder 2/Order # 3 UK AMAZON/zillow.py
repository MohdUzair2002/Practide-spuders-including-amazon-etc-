from urllib.request import Request
import scrapy
from read_files import read_csv
base_url=''
class ZillowSpider(scrapy.Spider):
    name = 'zillow'
    # allowed_domains = ['x']
    # start_urls = ['http://x/']
    def start_requests(self):
        print(self)
        for links in read_csv():
          yield scrapy.Request(links)
    def parse(self, response):
        yield{
    'que':response.xpath("//span[@class='Text-c11n-8-63-0__sc-aiai24-0 dpf__sc-1yftt2a-1 gbKiss iOiapS']")
        }