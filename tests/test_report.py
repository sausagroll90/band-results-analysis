import unittest
import sqlite3
from band_results import report


class TestFormatKeyValue(unittest.TestCase):
    def test_general_case(self):
        self.assertEqual(report.format_key_value("position", 4), "position: 4")

    def test_count(self):
        self.assertEqual(report.format_key_value("COUNT(*)", 20), "count: 20")


class TestFormatRowForConsole(unittest.TestCase):
    def test_format_row(self):
        test_row = {"band_name": "Black Dyke", "region": "Yorkshire"}
        expected = "band_name: Black Dyke\nregion: Yorkshire\n"
        self.assertEqual(report.format_row_for_console(test_row), expected)

    def test_count(self):
        test_row = {"region": "North West", "COUNT(*)": 2}
        expected = "region: North West\ncount: 2\n"
        self.assertEqual(report.format_row_for_console(test_row), expected)


class TestFormatRowForTxt(unittest.TestCase):
    def test_format_row(self):
        test_row = {"band_name": "Black Dyke", "region": "Yorkshire"}
        expected = "band_name: Black Dyke, region: Yorkshire\n"
        self.assertEqual(report.format_row_for_txt(test_row), expected)

    def test_count(self):
        test_row = {"region": "North West", "COUNT(*)": 2}
        expected = "region: North West, count: 2\n"
        self.assertEqual(report.format_row_for_txt(test_row), expected)

