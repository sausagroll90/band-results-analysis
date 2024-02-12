from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def get_data_from_row(row):
    row_data = {
        "position": row.contents[1].a.string,
        "band": row.contents[3].a.string,
        "conductor": row.contents[5].a.string,
        "draw": row.contents[7].a.string
    }
    return row_data


def get_results(url):
    hdr = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    request = Request(url, headers=hdr)

    page = urlopen(request)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    results_table = soup.main.div.contents[7].contents[7].tbody

    # results table is empty at even indices
    rows = [x for i, x in enumerate(results_table.children) if i % 2 == 1]
    results = list(map(get_data_from_row, rows))

    return results


def get_urls(number=None):
    url = "https://www.brassbandresults.co.uk/contests/national-finals-championship-section"

    hdr = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    request = Request(url, headers=hdr)

    page = urlopen(request)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    contests_table = soup.main.tbody
    events = contests_table.find_all("a", attrs={"class": "bbr-event"})
    urls = ["https://www.brassbandresults.co.uk" + x.get("href") for x in events]

    if number is None:
        return urls

    return urls[:number]


if __name__ == "__main__":
    print(get_urls())
