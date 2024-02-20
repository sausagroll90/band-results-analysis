import scraper
import db
import argparse


def main():
    parser = argparse.ArgumentParser(description="Gets results from given URL and stores them in bandresults.db")
    parser.add_argument("--init-db", help="Clear the entire database", action="store_true")
    parser.add_argument("-r", help="Scrape results from all pages linked to from the URL provided",
                        action="store_true")
    parser.add_argument("--url", help="The URL of the results page to be scraped")

    args = parser.parse_args()

    if args.init_db:
        db.init_db()

    if args.url is None:
        return

    if not args.r:
        results = scraper.get_results(args.url)
        for result in results:
            db.add_result(result, "bandresults.db")
    else:
        urls = scraper.get_urls(args.url)
        for url in urls:
            results = scraper.get_results(url)
            for result in results:
                db.add_result(result, "bandresults.db")


if __name__ == "__main__":
    main()
