from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def make_soup(url):
    hdr = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    request = Request(url, headers=hdr)
    page = urlopen(request)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    return soup


def get_data_from_row(row):
    row_data = dict()
    items = ("position", "band", "conductor", "draw")

    for item in items:
        try:
            row_data[item] = row.find("td", attrs={"class": f"bbr-{item}"}).a.string
            if item == "band":
                row_data["region"] = row.find("td", attrs={"class": "bbr-band"}).img["title"]
        except AttributeError:
            row_data[item] = ""
            if item == "band":
                row_data["region"] = ""

    return row_data


def get_year(url):
    return url.split("/")[-1].split("-")[0]


def get_contest(url):
    soup = make_soup(url)
    return soup.find("a", attrs={"class": "bbr-contest"}).string


def get_results(url):
    soup = make_soup(url)
    results_table = soup.main.div.contents[7].contents[7].tbody

    year = get_year(url)
    # results table is empty at even indices
    rows = [x for i, x in enumerate(results_table.children) if i % 2 == 1]
    results = list(map(get_data_from_row, rows))

    for result in results:
        result["year"] = year

    return results


def get_urls(url, number=None):
    soup = make_soup(url)
    contests_table = soup.main.tbody
    events = contests_table.find_all("a", attrs={"class": "bbr-event"})
    urls = ["https://www.brassbandresults.co.uk" + x.get("href") for x in events]

    if number is None:
        return urls

    return urls[:number]


if __name__ == "__main__":
    print(get_urls(5))
