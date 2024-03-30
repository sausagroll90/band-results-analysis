import sqlite3


def init_db():
    con = sqlite3.connect("bandresults.db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS result")
    cur.execute("DROP TABLE IF EXISTS band")
    cur.execute(
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
    cur.execute("""       
                    CREATE TABLE band (
                        band_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE,
                        region TEXT
                    )""")


def add_result(result, db):
    con = sqlite3.connect(db)
    cur = con.cursor()

    cur.execute(
        "INSERT OR IGNORE INTO band (name, region) VALUES (?, ?)",
        (result["band"], result["region"]))

    (band_id,) = cur.execute("SELECT band_id FROM band WHERE name = ?",
                             (result["band"],)).fetchone()

    cur.execute(
        "INSERT INTO result (position, band_id, conductor, draw, year) VALUES(?, ?, ?, ?, ?)",
        (result["position"], band_id, result["conductor"], result["draw"], result["year"])
    )

    con.commit()


def get_results(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    results = cur.execute(
        """SELECT position, name, conductor, draw, year FROM result INNER JOIN band USING(band_id)"""
    ).fetchall()
    return results


def main():
    init_db()


def get_winners():
    con = sqlite3.connect("bandresults.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    results = cur.execute("SELECT name, conductor, year, draw FROM result JOIN band USING(band_id) WHERE position=1")
    rows = results.fetchall()
    return rows


if __name__ == "__main__":
    main()
