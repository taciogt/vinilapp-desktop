import unittest
import database


class DatabaseTests(unittest.TestCase):

    def test_check_if_singleton(self):
        db1 = database.get_db()
        db2 = database.get_db()
        self.assertEqual(db1, db2)
