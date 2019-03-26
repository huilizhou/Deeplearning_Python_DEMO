import mysql.connector

conn = mysql.connector.connect(
    user='root', password='', database='fruitpricedb')

cursor = conn.cursor()
# # 创建fruittb表:
# cursor.execute(
#     'create table fruittb (id varchar(20) primary key, name varchar(20),price double)')

# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('0', 'dongzao', '10.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('1', 'xiangjiao', '8.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('2', 'juzi', '6.5'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('3', 'pingguo', '12.8'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('4', 'huolongguo', '16.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('5', 'huanggua', '5.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('6', 'lajiao', '3.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('7', 'bailuobo', '3.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('8', 'buluo', '12.0'))
# cursor.execute('insert into fruittb (id, name,price) values (%s, %s,%s)',
#                ('9', 'hamigua', '16.0'))


# print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select price from fruittb where id = %s', ('3',))

# cursor.execute('select * from fruittb where name = %s', ('xiangjiao',))
values = cursor.fetchall()
# print(values)
print(values[0][0])
# 关闭Cursor和Connection:
cursor.close()
conn.close()
