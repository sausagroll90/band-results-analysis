import scraper
import db


def main():
    bandresults_db = "bandresults.db"
    urls = scraper.get_urls(3)

    for url in urls:
        results = scraper.get_results(url)

        for result in results:
            db.add_result(result, bandresults_db)

    print(db.get_results(bandresults_db))


if __name__ == "__main__":
    main()
