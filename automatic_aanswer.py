from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profi = {}
    profi['title'] = 'Анкета космонавта'
    profi['surname'] = 'Readle'
    profi['name'] = 'Mark'
    profi['education'] = 'высшее'
    profi['profession'] = 'инженер'
    profi['sex'] = 'male'
    profi['motivation'] = 'Мечтал побывать на Марсе всю свою жизнь'
    profi['ready'] = 'True'
    return render_template('automatic_answer.html', **profi)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
