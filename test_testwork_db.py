# -*- coding: utf-8 -*-
import unittest


from testwork_db import HandMadeDB


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
        base.delete('один')
        self.assertNotIn('один', base.db)

    def test_read(self):
        """
        Функция, тестирующая чтение значений из базы данных
        :return:
        """
        base.update('один', 1)
        value = base.read('один')
        self.assertEqual(value, 1)


if __name__ == '__main__':
    unittest.main()