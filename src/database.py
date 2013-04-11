# coding=utf-8


def get_db():
    if Database._db is not None:
        return Database._db
    else:
        Database._db = Database()
        return Database._db


class Database():
    _db = None
