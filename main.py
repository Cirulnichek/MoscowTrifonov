from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main_window():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    a = '''Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!'''
    return '</br>'.join(a.split('\n'))


@app.route('/image_mars')
def image_mars():
    result = '<title>Привет, Марс!</title>'
    result += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" ' \
              'rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" ' \
              'crossorigin="anonymous">'
    result += '<h1 style="color:red">Жди нас, Марс!</h1>'
    result += '<img src="https://kipmu.ru/wp-content/uploads/pchmrskrs.jpg" alt="Марс"></br>'
    result += '<p class="bg-primary">Человечество вырастает из детства</p>'
    result += '<p class="bg-secondary"Человечеству мала одна планета</p>'
    result += '<p class="bg-danger">Мы сделаем обитаемыми безжизненные пока планеты</p>'
    result += '<p class="bg-warning">И начнем с Марса!</p>'
    result += '<p class="bg-info">Присоединяйся!</p>'
    return result


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')