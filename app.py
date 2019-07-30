# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_cors import CORS
from wtforms import Form, StringField, validators


from testwork_db import HandMadeDB


# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app)


base = None


class UpdateForm(Form):
    "Форма для добавления данных"
    key = StringField('key', [validators.DataRequired()])
    value = StringField('value', [validators.DataRequired(), validators.AnyOf(int, str, list)])


@app.route('/', methods=['GET'])
def home():
    """
    Функция, которая загружает пользователю разводящую страницу
    :return:
    """
    return render_template('index.html')


@app.route('/create', methods=['GET'])
def create():
    """
    Функция, которая создает и возвращает базу данных
    :return:
    """
    global base
    base = HandMadeDB()
    base = HandMadeDB().db
    return render_template('create.html'), base


@app.route('/update')
def update_page():
    return render_template('update.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    """
    Функция, которая добавляет пару ключ-значение в базу данных
    :return:
    """
    global base
    # form = UpdateForm()
    key = request.form['key']
    value = request.form['value']
    # base.update(key, value)
    base[key] = value
    message = 'В базу данных добавлена пара {key: value}'
    return render_template('update.html', message=message), base


@app.route('/read')
def read_page():
    return render_template('read.html')

@app.route('/read', methods=['GET', 'POST'])
def read():
    """
    Функция, которая читает значение из базы данных и возвращает на страницу
    :return:
    """
    try:
        key = request.form['key']
        # value = base.read(key)
        value = base[key]
        return render_template('read.html', value=value)
    except KeyError:
        error = 'Произошла ошибка, возможно запрашиваемого элемента нет в базе'
        return render_template('read.html', error=error)

@app.route('/delete')
def delete_page():
    return render_template('delete.html')

@app.route('/delete', methods=['POST'])
def delete():
    """
    Функция, которая удаляет пару ключ-значение из базы данных
    :return:
    """
    global base
    try:
        key = request.form['key']
        # base.delete(key)
        base.pop(key)
        message = 'Из базы удалено значение для ключа {}'.format(key)
        return render_template('delete.html', message=message), base
    except KeyError:
        error = 'Произошла ошибка, возможно запрашиваемого элемента нет в базе'
        return render_template('delete.html', error=error), base

if __name__ == '__main__':
    app.run(port='5000')
