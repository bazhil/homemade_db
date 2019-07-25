# -*- coding: utf-8 -*-
import json
import logging
import datetime
import unittest

class HandMadeDB:
    """
    Класс самодельной базы данных с простыми операциями CRUD
    """
    def __init__(self):
        self.db = {}

    logging.basicConfig(filename='db_activity.log', level=logging.INFO)

    def open(self):
        """
        Функция, которая открывает сохраненную базу данных формата JSON
        :return:
        """
        self.db = open('db.json')
        logging.info(
            str(datetime.datetime.today()) + ' ' + 'Пользователь загрузил сохраненную базу данных')
        return self.db

    def read(self, key=str):
        """
        Функция, которая считывает значение базы данных для ключа
        :param db:
        :param key:
        :return:
        """
        if key in self.db:
            return self.db[key]
        elif key not in self.db:
            print('В базе данных нет такого ключа')
        logging.info(
            str(datetime.datetime.today()) + ' ' + 'Пользователь искал значение для ключа "{}" в базе данных'.format(
                key))

    def update(self, key=str, value=(str or int or list)):
        """
        Функция, которая вставляет в базу ключ-значение
        :param db: база данных
        :param key: ключ
        :param value: значение
        :return: обновленная база данных
        """
        if key not in self.db:
            self.db[key] = value
            logging.info(
                str(
                    datetime.datetime.today()) + ' ' + 'Пользователь вставил значение для ключа "{}" = {} в базу данных'.format(
                    key, value))
        else:
            answer = input('Данный ключ уже содержится в базе данных, вы уверены, что хотите перезаписать [y/n]: ')

            if answer == 'y':
                self.db[key] = value
                logging.info(
                    str(
                        datetime.datetime.today()) + ' ' + 'Пользователь перезаписал значение для ключа "{}" = {} в базу данных'.format(
                        key, value))
            elif answer == 'n':
                key = input('Введите ключ повторно: ')
                self.db[key] = value
        self.save()
        logging.info(
            str(datetime.datetime.today()) + ' ' + 'Пользователь вставил значение для ключа "{}" в базу данных'.format(
                key))
        return self.db

    def delete(self, key=str):
        """
        Функция, которая удаляет пару ключ-значение по переданному ключу
        :param db: база данных
        :param key: ключ
        :return: база данных
        """
        try:
            del self.db[key]
        except KeyError:
            print('В базе данных нет такого ключа')
        self.save()
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь удалил значения для ключа "{}" из базы данных'.format(key))
        return self.db

    def save(self):
        """
        Функция, которая сохраняет базу данных в JSON
        :param db:
        :return:
        """
        with open('db.json', 'w') as d:
            json.dump(self.db, d, ensure_ascii=False, indent=2)
        logging.info(str(datetime.datetime.today()) + ' ' + 'Пользователь сохранил изменения в базе данных')

if __name__ == '__main__':
    base = HandMadeDB()

    class TestDB(unittest.TestCase):
        """
        Тестирующий класс
        """
        def test_update(self):
            """
            Функция, тестирующая вставку значений в базу данных
            :return:
            """
            base.update('один', 1)
            self.assertEqual(base.db, {'один': 1})

        def test_delete(self):
            """
            Функция, тестирующая удаление значений из базы данных
            :return:
            """
            base.update('один', 1)
            self.assertEqual(base.db, {'один': 1})
            base.delete('один')
            self.assertNotIn('один', base.db)

    unittest.main()



