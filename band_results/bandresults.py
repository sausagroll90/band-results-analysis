import scraper
import db


def main():
    # urls = scraper.get_urls(10)
    #
    # for url in urls:
    #     results = scraper.get_results(url)
    #
    #     for result in results:
    #         print(result)
    #         db.add_result(result)

    print(db.get_results())


if __name__ == "__main__":
    main()
