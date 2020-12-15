import scrapy
from ..items import YunshangwangItem


class YunSpider(scrapy.Spider):
    name = 'yun'
    # allowed_domains = ['yun.com']
    start_urls = ['http://www.ynshangji.com/qiye/']
    base_http = 'http://www.ynshangji.com'

    def parse(self, response):
        links = response.xpath('//div[@class="fl J-mainNav"]/ul/li/a/@href').getall()
        for link in links:
            # print(self.base_http+link)
            yield scrapy.Request(url=self.base_http+link, callback=self.parse_list)
            # break
    
    def parse_list(self, response):
        com_links = response.xpath('//div[@class="description"]/div[@class="til"]/a/@href').getall()
        for com_link in com_links:
            # print(self.base_http + com_link)
            yield scrapy.Request(url=self.base_http+com_link, callback=self.parse_detail)
        pages = response.xpath('//div[@class="paging mb30"]/a/@href').getall()
        for page in pages:
            next_page = page.replace('..', self.base_http)
            yield scrapy.Request(url=next_page, callback=self.parse_list)
            
    def parse_detail(self, response):
        com_name = response.xpath('//div[@class="aiMain"]/ul/li[1]/text()').get()
        conn_name = response.xpath('//div[@class="aiMain"]/ul/li[2]/text()').get()
        com_addr = response.xpath('//div[@class="aiMain"]/ul/li[3]/text()').get()
        conn_tel = response.xpath('//div[@class="aiMain"]/ul/li[4]/text()').get()
        conn_mobile = response.xpath('//div[@class="aiMain"]/ul/li[6]/text()').get()
        conn_province = response.xpath('//div[@class="aiMain"]/ul/li[7]/a[1]/text()').get()
        conn_city = response.xpath('//div[@class="aiMain"]/ul/li[7]/a[2]/text()').get()
        # print(com_name, conn_name, com_addr, conn_tel, conn_mobile, conn_province, conn_city)
        item = YunshangwangItem()
        item['com_name'] = com_name
        item['conn_name'] = conn_name
        item['com_addr'] = com_addr
        item['conn_tel'] = conn_tel
        item['conn_mobile'] = conn_mobile
        item['conn_province'] = conn_province
        item['conn_city'] = conn_city
        yield item
