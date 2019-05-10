from flask import Flask, render_template
from chendbmanage import ChenUseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'root',
                          'password': '',
                          'database': 'chenriyuelakedb', }


@app.route('/')
def hello()->str:
    return "Hello World from Flask"


@app.route('/devshow')
def devshow() -> 'html':
    return render_template('devshow.html')


@app.route('/devinfo')
def devinfo() -> 'html':
    with ChenUseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select recordtime, light, temperature, 
       humidity from sensordata order by id desc limit 1"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    recordtime = str(contents[0][0]).replace(' ', '\b')
    #recordtime = str(contents[0][0]).replace(' ','')
    light = contents[0][1]
    temperature = contents[0][2]
    humidity = contents[0][3]
    return render_template('devinfo.html', the_recordtime=recordtime, the_light=light,
                           the_temperature=temperature, the_humidity=humidity,)


if __name__ == "__main__":
    app.run()
