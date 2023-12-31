import scraper
import db


def main():
    url = "https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2023-10-21"

    results = scraper.get_results(url)

    db.init_db()

    for result in results:
        db.add_result(result)

    print(db.get_results())


if __name__ == "__main__":
    main()
