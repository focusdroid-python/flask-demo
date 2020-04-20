# coding:utf-8

import unittest
from author_book import Author, db, app


class DatebaseTest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:mysql@127.0.0.1:3306/flask_test'

    def test_add_author(self):
        """测试添加作者的数据库操作"""
        author = Author(name='focusdroid', email='itcast@163.com', mobile='15701223123')
        db.session.add(author)
        db.session.commit()

        import time
        time.sleep(10000)

        result_author = Author.query.filter_by(name='focusdroid').first()
        self.assertIsNotNone(result_author)

    def teatDown(self):
        '''在所有的测试执行后，通常用来清理操作'''
        db.session.remove()
        db.drop_all()