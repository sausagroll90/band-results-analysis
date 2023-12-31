from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = "https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2023-10-21"
hdr = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
request = Request(url, headers=hdr)

page = urlopen(request)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
results_table = soup.main.div.contents[7].contents[7].tbody

# results table is empty at even indices
rows = [x for i, x in enumerate(results_table.children) if i % 2 == 1]


def get_data_from_row(row):
    row_data = {
        "position": row.contents[1].a.string,
        "band": row.contents[3].a.string,
        "conductor": row.contents[5].a.string,
        "draw": row.contents[7].a.string
    }
    return row_data


print(get_data_from_row(rows[1]))
