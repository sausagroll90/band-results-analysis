import unittest
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from band_results import scraper


class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2023-10-21"
        self.soup = scraper.make_soup(self.url)

    def test_get_data_from_row(self):
        results_table = self.soup.main.div.contents[7].contents[7].tbody
        row = results_table.contents[1]

        data = scraper.get_data_from_row(row)
        self.assertEqual(data, {
            "position": "1",
            "band": "Black Dyke",
            "conductor": "Nicholas Childs",
            "draw": "17"
        })

    def test_get_results(self):
        results = scraper.get_results(self.url)
        self.assertEqual(results[:3], [
            {
                "position": "1",
                "band": "Black Dyke",
                "conductor": "Nicholas Childs",
                "draw": "17"
            },
            {
                "position": "2",
                "band": "Fodens",
                "conductor": "Russell Gray",
                "draw": "20"
            },
            {
                "position": "3",
                "band": "Cory",
                "conductor": "Philip Harper",
                "draw": "12"
            }
        ])


class GetUrlTestCase(unittest.TestCase):
    def test_get_5_urls(self):
        target = ['https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2023-10-21',
                  'https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2022-10-15',
                  'https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2021-10-02',
                  'https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2020-10-10',
                  'https://www.brassbandresults.co.uk/contests/national-finals-championship-section/2019-10-12']

        self.assertEqual(scraper.get_urls(5), target)

    def test_get_all_urls(self):
        soup = scraper.make_soup("https://www.brassbandresults.co.uk/contests/national-finals-championship-section")
        contests_table = soup.main.tbody
        events = contests_table.find_all("a", attrs={"class": "bbr-event"})

        self.assertEqual(len(events), len(scraper.get_urls()))


if __name__ == '__main__':
    unittest.main()