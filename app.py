# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template, flash, redirect, url_for
from flask_cors import CORS


from testwork_db import HandMadeDB


# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# enable CORS
CORS(app)


base = None


# class MyForm(FlaskForm):
#     "Класс формы"
#
#     def validate_value(self):
#         """
#         Функция, которая проверяет значение поля value
#         :return:
#         """
#         # смотри https://wtforms.readthedocs.io/en/stable/forms.html
#         pass
#
#     key = StringField('name', validators=[DataRequired()])
#     value = StringField('name', validators=[DataRequired()])


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
    base = HandMadeDB().db
    return render_template('create.html', base=base), base


@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/update', methods=['POST'])
def get_update():
    """
    Функция, которая добавляет пару ключ-значение в базу данных
    :return:
    """
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        base.update(key, value)
    print(request.form)
    return render_template('app_data.html', key=key, value=value), base


@app.route('/read', methods=['GET'])
def read():
    """
    Функция, которая читает значение из базы данных по ключу
    :return:
    """
    # key = request.form['key']
    # value = base[key]
    return render_template('read.html')



@app.route('/delete', methods=['GET', 'POST'])
def delete():
    """
    Функция, которая удаляет пару ключ-значение из базы данных
    :return:
    """

    return render_template('delete.html')

if __name__ == '__main__':
    app.run(port='5000')
