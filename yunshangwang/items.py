# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YunshangwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    com_name = scrapy.Field()
    conn_name = scrapy.Field()
    com_addr = scrapy.Field()
    conn_tel = scrapy.Field()
    conn_mobile = scrapy.Field()
    conn_province = scrapy.Field()
    conn_city = scrapy.Field()

    '''
    CREATE TABLE `yunshangwang` (
      `com_name` varchar(50) DEFAULT NULL COMMENT '公司名称',
      `conn_name` varchar(30) DEFAULT NULL,
      `com_addr` varchar(200) DEFAULT NULL,
      `conn_tel` varchar(30) DEFAULT NULL,
      `conn_mobile` varchar(30) DEFAULT NULL,
      `conn_province` varchar(10) DEFAULT NULL,
      `conn_city` varchar(10) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8

    '''
