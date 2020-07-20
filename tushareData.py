# import tushare as ts
# from sqlalchemy import create_engine
# import pymysql
# # ts.set_token('d49e3859a3841cce97588cf8681d6f06628788080cc8f7a73af8fcaf')
# # pro = ts.pro_api()
# # df = pro.index_basic(market='SW')
# # print(df)
# # engine = create_engine('mysql+pymysql://root:Wshuguang1@localhost/findata?charset=utf8')
# # df.to_sql('index_basic', engine, if_exists='append')

import tushare as ts
import pymysql

import requests
from sqlalchemy import desc, create_engine, Column, Integer, String, Text  # 降序、连接路径、列、字符串、文本
from sqlalchemy.orm import scoped_session, sessionmaker  # 代理模式、数据库连接的媒（手机）；engine号码
from sqlalchemy.ext.declarative import declarative_base  # 声明类映射类到表的关系
from sqlalchemy import create_engine

# ts.set_token('d49e3859a3841cce97588cf8681d6f06628788080cc8f7a73af8fcaf')
# df = ts.pro_api()
# engine = create_engine('mysql+pymysql://root:Wshuguang1@localhost:3306/findata?charset=utf8')
# data = df.stock_basic()
# data.to_sql('stock_basic', engine, if_exists='append')

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Wshuguang1',
                             db='stock',
                             port=3306,
                             charset='utf8')
try:
    # 获取一个游标
    with connection.cursor() as cursor:
        sql = 'select * from stock_basic'
        cout = cursor.execute(sql)
        print("数量： " + str(cout))

        for row in cursor.fetchall():
            # 注意int类型需要使用str函数转义
            print("ID: " + str(row[0]) + '  名字： ' + row[1] + "  性别： " + row[2])
        connection.commit()

finally:
    connection.close()


