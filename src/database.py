# coding=utf-8


def get_db():
    try:
        singleton = Database()
    except Database as db:
        singleton = db
    return singleton


class Database():
    _db = None

    def __init__(self):
        if Database._db is not None:
            raise Database._db
        Database._db = self


class DatabaseError(Exception):
    pass
