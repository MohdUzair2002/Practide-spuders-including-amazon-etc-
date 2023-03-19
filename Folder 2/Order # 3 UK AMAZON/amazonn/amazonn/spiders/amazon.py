from cgitb import text
from unicodedata import name
from urllib import response
import scrapy
from read_files import read_csv
import csv
base_url = ""

class AmazonnSpider(scrapy.Spider):
    name = 'amazon'
    i=0
##    allowed_domains = ['https://www.amazon.co.uk']
    
    # start_urls = ["https://www.amazon.co.uk/s?k=samsung+galaxy+s8&crid=3FAAY7NY4MKM&sprefix=\
    # # samsung+galaxy+s8%2Caps%2C76"]
    def start_requests(self):
        # df=pd.read_csv('Zillow.csv')
        for links in read_csv():
            yield scrapy.Request(links)
    def  parse(self, response):
        No='None'
        try:
         
         off_market=response.xpath("//span[@class='Text-c11n-8-63-0__sc-aiai24-0 dpf__sc-1yftt2a-1 gbKiss iOiapS']/text()").get()
         yield{
              'link':response.txt,
               'offmarket':off_market

          }
        except:
            yield{
                'link':response,
                'ofmarket':No
            }
        with open('zil.csv', 'w', newline='', encoding='UTF8') as csvfile:
            fieldnames = ['links', 'offmarket']
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            next(writer.writerow([response,off_market]))
            
           
            # f=open("Data.csv","a")
    # def parse(self, response):
        
    #     listings=response.xpath("//div[@class='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16']")
    #     for list in listings:
    #         name=list.xpath(".//*[@class='a-size-medium a-color-base a-text-normal']/text()").extract()
    #         # print(name)
    #         price=list.xpath(".//*[@class='a-offscreen']/text()").get()
    #         # print(price)
    #         mainlink="https://www.amazon.co.uk/"
    #         link=list.xpath(".//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']/@href").get()
    #         LINK=(mainlink+link)
    #         # for i in range(16):
    #         yield{
    #             'name':name,
    #             'price':price,
    #            ' LINKS':LINK
    #         }
    #     print(AmazonnSpider.start_urls[0])
    #     page_2=AmazonnSpider.start_urls[0]+'&page=2'
    #     print(page_2)
    #     if AmazonnSpider.i<=1:
    #          AmazonnSpider.i+=1
    #          yield  response.follow(page_2,callback=self.parse)