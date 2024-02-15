import unittest
import sqlite3
from band_results import db


# noinspection PyMethodMayBeStatic
class QueryDBTestCase(unittest.TestCase):
    def init_db(self):
        self.con = sqlite3.connect("test.db")
        self.cur = self.con.cursor()

        self.cur.execute("DROP TABLE IF EXISTS result")
        self.cur.execute("DROP TABLE IF EXISTS band")
        self.cur.execute(
            """CREATE TABLE result (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                position INTEGER,
                band_id INTEGER NOT NULL,
                conductor TEXT,
                draw INTEGER,
                year INTEGER,
                FOREIGN KEY (band_id)
                    REFERENCES band (band_id)
            )""")
        self.cur.execute("""       
                CREATE TABLE band (
                    band_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    region TEXT
                )""")

    def add_data(self):
        self.cur.execute('INSERT INTO band (name, region) VALUES ("Black Dyke", "Yorkshire")')
        self.cur.execute("""INSERT INTO result (position, band_id, conductor, draw, year)
            VALUES (1, 1, "Nicholas Childs", 17, 2023)""")

        self.con.commit()

    def setUp(self):
        self.init_db()
        self.add_data()

    def test_get_results(self):
        test_data = [(1, "Black Dyke", "Nicholas Childs", 17, 2023)]
        self.assertEqual(test_data, db.get_results("test.db"))

    def test_add_result_existing_band(self):
        db.add_result({
                "position": "3",
                "band": "Black Dyke",
                "conductor": "Nicholas Childs",
                "draw": "10",
                "region": "Yorkshire",
                "year": "2015"
            }, "test.db")

        (num_bands,) = self.cur.execute("SELECT COUNT(1) FROM band").fetchone()
        self.assertEqual(1, num_bands)
        self.assertEqual([
            (1, 1, 1, "Nicholas Childs", 17, 2023),
            (2, 3, 1, "Nicholas Childs", 10, 2015)
        ], self.cur.execute("SELECT * FROM result").fetchall())

    def test_add_result_new_band(self):
        db.add_result({
            "position": "2",
            "band": "Foden's",
            "conductor": "Russell Gray",
            "draw": "20",
            "region": "North West",
            "year": "2023"
        }, "test.db")

        (num_bands,) = self.cur.execute("SELECT COUNT(1) FROM band").fetchone()
        self.assertEqual(2, num_bands)
        self.assertEqual([
            (1, "Black Dyke", "Yorkshire"),
            (2, "Foden's", "North West")
        ], self.cur.execute("SELECT * FROM band").fetchall())
        self.assertEqual([
            (1, 1, 1, "Nicholas Childs", 17, 2023),
            (2, 2, 2, "Russell Gray", 20, 2023)
        ], self.cur.execute("SELECT * FROM result").fetchall())


if __name__ == '__main__':
    unittest.main()
