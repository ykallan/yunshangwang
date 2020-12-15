import pymysql

conn = pymysql.Connect(
            host='localhost',
            port=3306,
            database='scrapy',
            user='root',
            passwd='root',
            charset='utf8',
        )
cursor = conn.cursor()

sql = '''SELECT * FROM yunshangwang WHERE conn_name = '李长华' AND conn_mobile = '13838785333';'''

result = cursor.execute(sql)
print(result)
