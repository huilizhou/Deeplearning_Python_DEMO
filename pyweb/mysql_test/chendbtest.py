from chendbmanage import ChenUseDatabase

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': '',
            'database': 'chenriyuelakedb'}
with ChenUseDatabase(dbconfig) as cursor:
    _SQL = """select recordtime, light, temperature,humidity from sensordata order by id desc limit 1"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
    print(contents)
