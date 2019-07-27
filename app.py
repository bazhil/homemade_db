# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
# from app import app, db, lm, oid
# from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required
from flask import render_template, flash, redirect
# from forms import LoginForm

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

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
    html = """
    <h1>Тестовая самописная база данных</h1>
    <p>Данное приложение предоставляет API для демонстрации возможностей вышеуказанной БД:</p>
    <ol>
        <li><a href="http://localhost:5000/create">Создание базы данных</a></li>
        <li><a href="http://localhost:5000/read">Получение элемента из базы данных</a></li>
        <li><a href="http://localhost:5000/update">Добавление элемента в базу данных</a></li>
        <li><a href="http://localhost:5000/delete">Удаление элемента из базы данных</a></li>
    </ol>
    """
    return html

@app.route('/create', methods=['GET'])
def create():
    """
    Функция, которая создает и возвращает базу данных
    :return: база данных
    """
    global base
    base = HandMadeDB()
    html = """
    <h1>Создание базы данных</h1>
    <p>База данных создана</p>
    <p>На данный момент в базе данных находится {} элементов.</p>
    """.format(len(base.db))
    return html

@app.route('/read', methods=['GET', 'POST'])
def read():
    """
    Функция, которая читае значение из базы данных по ключу
    :return: база данных
    """
    html = """
        <h1>Чтение значения из базы по ключу</h1>
        <form>
            <p>Введите ключ</p>
            <input type="text" name="key" id="dataKey" size="20" placeholder="Ключ">
            <input type="button" id="spotButton" value="Ввести">
        </form>
        """
    return html

@app.route('/update', methods=['GET', 'POST'])
def update():
    """
    Функция, которая добавляет пару ключ-значение в базу данных
    :return: база данных
    """
    html = """
    <h1>Добавление значения в базу</h1>
    <form>
        <p>Введите пару ключ-значение</p>
        <input type="text" name="key" id="dataKey" size="20" placeholder="Ключ">
        <input type="text" name="value" id="dataValue" size="20" placeholder="Значение">
        <input type="button" id="spotButton" value="Ввести">
    </form>
    """
    return html

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    """
    Функция, которая удаляет пару ключ-значение из базы данных
    :return: база данных
    """
    html = """
        <h1>Удаление значения из базы</h1>
        <form>
            <p>Введите ключ</p>
            <input type="text" name="key" id="dataKey" size="20" placeholder="Ключ">
            <input type="button" id="spotButton" value="Удалить">
        </form>
        """
    return html

if __name__ == '__main__':
    app.run(port='5000')
