#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# # 执行一条SQL语句，创建fruittb表:
# cursor.execute(
#     'create table fruittb (id varchar(20) primary key, name varchar(20),price double)')
# # 继续执行一条SQL语句，插入一条记录:
# # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'0\', \'dongzao\', \'10.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'1\', \'xiangjiao\', \'8.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'2\', \'juzi\', \'6.5\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'3\', \'pingguo\', \'12.8\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'4\', \'huolongguo\', \'16.0\')')

# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'5\', \'huanggua\', \'5.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'6\', \'lajiao\', \'3.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'7\', \'bailuobo\', \'3.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'8\', \'buluo\', \'12.0\')')
# cursor.execute(
#     'insert into fruittb (id, name,price) values (\'9\', \'hamigua\', \'16.0\')')


# # 通过rowcount获得插入的行数:
# print('rowcount =', cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select price from fruittb where id=?', '2')
# 获得查询结果集:
values = cursor.fetchall()
print(values[0][0])
cursor.close()
conn.close()
