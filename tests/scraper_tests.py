import unittest
from band_results import scraper
from bs4 import BeautifulSoup

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
            "draw": "17",
            "region": "Yorkshire"
        })

    def test_get_data_from_row_empty(self):
        newsoup = BeautifulSoup('<tr><td class="bbr-position"><span></span></td><td class="bbr-band"><span></span></td><td class="bbr-conductor"><span></span></td><td class "bbr-draw"><span></span></td></tr>', "html.parser")
        data = scraper.get_data_from_row(newsoup)
        self.assertEqual(data, {
            "position": "",
            "band": "",
            "conductor": "",
            "draw": "",
            "region": ""
        })

    def test_get_year(self):
        self.assertEqual(scraper.get_year(self.url), "2023")

    def test_get_results(self):
        results = scraper.get_results(self.url)
        self.assertEqual(results[:3], [
            {
                "position": "1",
                "band": "Black Dyke",
                "conductor": "Nicholas Childs",
                "draw": "17",
                "region": "Yorkshire",
                "year": "2023"
            },
            {
                "position": "2",
                "band": "Fodens",
                "conductor": "Russell Gray",
                "draw": "20",
                "region": "North West",
                "year": "2023"
            },
            {
                "position": "3",
                "band": "Cory",
                "conductor": "Philip Harper",
                "draw": "12",
                "region": "Wales",
                "year": "2023"
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
