# coding=utf-8

import unittest
# tácio: por que eu preciso desse 'import database' antes da linha abaixo dela
# import database
from src import database


class DatabaseTests(unittest.TestCase):

    def test_check_if_singleton(self):
        db1 = database.get_db()
        db2 = database.get_db()
        self.assertEqual(db1, db2)

        try:
            Database()
            self.fail()
        except:
            pass
