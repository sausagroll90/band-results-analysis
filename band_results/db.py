import sqlite3


def init_db():
    con = sqlite3.connect("bandresults.db")
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS result")
    cur.execute(
        """CREATE TABLE result (
            position INTEGER PRIMARY KEY,
            band TEXT UNIQUE NOT NULL,
            conductor TEXT,
            draw INTEGER UNIQUE
        )"""
    )


def add_result(result):
    con = sqlite3.connect("bandresults.db")
    cur = con.cursor()

    cur.execute(
        "INSERT INTO result (position, band, conductor, draw) VALUES(?, ?, ?, ?)",
        (result["position"], result["band"], result["conductor"], result["draw"])
    )

    con.commit()


def get_results():
    con = sqlite3.connect("bandresults.db")
    cur = con.cursor()
    results = cur.execute(
        """SELECT * FROM result
            WHERE position <= 3"""
    ).fetchall()
    return results


def main():
    init_db()


if __name__ == "__main__":
    main()