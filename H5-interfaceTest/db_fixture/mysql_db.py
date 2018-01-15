# -*- coding:utf-8 -*-
__auth__ = 'dingxd'
import mysql.connector
import os,sys
import configparser

base_dir = str(os.path.dirname(os.path.dirname(__file__))).replace('\\','/')
file_path = base_dir + '/configuration/db_config.ini'
print(file_path)

cf = configparser.ConfigParser()
cf.read(file_path,encoding='utf-8')
db='mysqlconf'

class DB():
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**(dict(cf[db])))
            self.cursor = self.conn.cursor()
            print('success')
        except Exception as e:
            print("Error:%s" % e)
            sys.exit()

    def select(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            print(result)
            print(result[0][1])
            return result
        except Exception as  e:
            print("query failed{}".format(e))


if __name__=='__main__':
    getdb=DB()
    select_sql = "select * from user_info where phone='18600000002'"
    getdb.select(select_sql)
