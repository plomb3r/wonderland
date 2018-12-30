import sqlite3

from source.config_reader import ConfigReader

config = ConfigReader()


class SqlWorker:
    def __init__(self, db_path=config.config_get("db_connect", 'db_file_path')):
        self.db_path = db_path

    def connect_db(self):
        conn = sqlite3.connect(self.db_path)
        return conn, conn.cursor()

    def select(self, element):
        conn, cursor = self.connect_db()
        cursor.execute(element)
        results = cursor.fetchall()
        conn.close()
        return results

    def insert(self, element):
        conn, cursor = self.connect_db()
        cursor.execute(element)
        conn.commit()
        conn.close()
