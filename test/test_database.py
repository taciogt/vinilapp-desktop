# coding=utf-8

import unittest
from vinilapp import db


class DatabaseTests(unittest.TestCase):

    def test_check_db(self):
        self.assertIsNotNone(db)

    def test_songs_table(self):
        pass
