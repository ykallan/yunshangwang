# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class YunshangwangPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.conn.ping(reconnect=True)
        try:
            sql = '''SELECT * FROM yunshangwang WHERE com_name='{}' AND conn_name='{}' AND conn_mobile='{}';'''.format(
                                        item['com_name'],
                                        item['conn_name'],
                                        item['conn_mobile'])
            result = self.cursor.execute(sql)
            # print(result)
            # print(sql)
            if result == 0:
                self.cursor.execute('''INSERT INTO yunshangwang(com_name, conn_name, com_addr, conn_tel, conn_mobile,
                conn_province, conn_city) VALUES(%s, %s, %s, %s, %s, %s, %s)''',
                                    (item['com_name'], item['conn_name'], item['com_addr'], item['conn_tel'],
                                     item['conn_mobile'],
                                     item['conn_province'], item['conn_city']))
                self.conn.commit()
                return item
            else:
                print('has saved this info~')
                return item
        except Exception as e:
            print(e)
            return item

