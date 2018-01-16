# -*- coding: utf-8 -*-

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
import json,MySQLdb,MySQLdb.cursors

#要给连接的数据库设置编码charset = utf
con = MySQLdb.connect(host='127.0.0.1',port = 3306,user='root',db='test',charset='utf8',cursorclass = MySQLdb.cursors.DictCursor)
con.autocommit(True)
cur = con.cursor()

f = open('./movie.json','r')
# 把字符串解析成json 数据 
d = json.loads(f.readline())
f.close()
#sql语句在使用的时候不能以前的字符串格式化的写法了，而是两个参数的形式来书写

for value in d:
	sql= 'insert into doubanm1 (title,rate) values (%s,%s)'
	param = (value['title'],value['rate'])
	try:
		cur.execute(sql,param)
	except:
		con.rollback()

cur.close()
con.close()			