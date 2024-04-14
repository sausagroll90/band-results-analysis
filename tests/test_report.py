import unittest
from unittest.mock import patch
import sqlite3
import csv
from band_results import report


class TestFormatKeyValue(unittest.TestCase):
    def test_general_case(self):
        self.assertEqual(report.format_key_value("position", 4), "position: 4")

    def test_count(self):
        self.assertEqual(report.format_key_value("COUNT(*)", 20), "count: 20")


class TestFormatRowForConsole(unittest.TestCase):
    def test_simple_row(self):
        test_row = {"band_name": "Black Dyke", "region": "Yorkshire"}
        expected = "band_name: Black Dyke\nregion: Yorkshire\n"
        self.assertEqual(report.format_row_for_console(test_row), expected)

    def test_count(self):
        test_row = {"region": "North West", "COUNT(*)": 2}
        expected = "region: North West\ncount: 2\n"
        self.assertEqual(report.format_row_for_console(test_row), expected)


class TestFormatRowForTxt(unittest.TestCase):
    def test_simple_row(self):
        test_row = {"band_name": "Black Dyke", "region": "Yorkshire"}
        expected = "band_name: Black Dyke, region: Yorkshire\n"
        self.assertEqual(report.format_row_for_txt(test_row), expected)

    def test_count(self):
        test_row = {"region": "North West", "COUNT(*)": 2}
        expected = "region: North West, count: 2\n"
        self.assertEqual(report.format_row_for_txt(test_row), expected)


class TestSaveRowsToTxt(unittest.TestCase):
    def test_save_rows_to_txt(self):
        test_rows = [
            {"band_name": "Black Dyke", "region": "Yorkshire"},
            {"band_name": "Foden's", "region": "North West"},
        ]
        report.save_rows_to_txt("tests/test.txt", test_rows)
        with open("tests/test.txt") as f:
            file_contents = f.read()
        expected = "band_name: Black Dyke, region: Yorkshire\nband_name: Foden's, region: North West\n"

        self.assertEqual(file_contents, expected)


class TestSaveRowsToCsv(unittest.TestCase):
    def test_simple_rows(self):
        test_rows = [
            {"band_name": "Black Dyke", "region": "Yorkshire"},
            {"band_name": "Foden's", "region": "North West"},
        ]
        expected = [
            ["band_name", "region"],
            ["Black Dyke", "Yorkshire"],
            ["Foden's", "North West"],
        ]

        report.save_rows_to_csv("tests/test.csv", test_rows)

        with open("tests/test.csv") as csvfile:
            reader = csv.reader(csvfile)
            actual = [row for row in reader]

        self.assertListEqual(actual, expected)

    def test_row_with_count(self):
        test_rows = [
            {"region": "Yorkshire", "COUNT(*)": 4},
            {"region": "North West", "COUNT(*)": 3},
        ]
        expected = [["region", "count"], ["Yorkshire", "4"], ["North West", "3"]]

        report.save_rows_to_csv("tests/test.csv", test_rows)

        with open("tests/test.csv") as csvfile:
            reader = csv.reader(csvfile)
            actual = [row for row in reader]

        self.assertListEqual(actual, expected)


class TestSaveRowsToFile(unittest.TestCase):
    @patch("band_results.report.save_rows_to_txt")
    def test_txt(self, mock_save_rows_to_txt):
        test_rows = {"band_name": "Foden's", "region": "North West"}
        report.save_rows_to_file("test.txt", test_rows)
        mock_save_rows_to_txt.assert_called_with("test.txt", test_rows)

    @patch("band_results.report.save_rows_to_csv")
    def test_csv(self, mock_save_rows_to_csv):
        test_rows = {"band_name": "Foden's", "region": "North West"}
        report.save_rows_to_file("test.csv", test_rows)
        mock_save_rows_to_csv.assert_called_with("test.csv", test_rows)

    def test_invalid_file_extension(self):
        test_rows = {"band_name": "Foden's", "region": "North West"}
        with self.assertRaises(ValueError):
            report.save_rows_to_file("test.rtf", test_rows)
