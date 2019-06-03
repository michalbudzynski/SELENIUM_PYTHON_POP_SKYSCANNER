# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.home_page import HomePage, HomePageSearchBox
from data_test import DataSearchBox


class SearchFlight(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skyscanner.pl/")

    def tearDown(self):

        self.driver.quit()

    def test_origin_destination_same_msg(self):
        search_box = HomePageSearchBox(self.driver)
        search_box.set_orgin("Katowice")
        search_box.set_destinantion("Katowice")
        search_box.click_search_flight()
        assert DataSearchBox.VALIDATION_MSG == search_box.get_flight_validation_msg()

    def test_change_flight(self):
        search_box = HomePageSearchBox(self.driver)
        search_box.set_orgin("Kraków")
        search_box.set_destinantion("Katowice")
        search_box.click_change_flight()
        assert 'Katowice (KTW)' == search_box.get_origin()

    def test_one_way_date(self):
        search_box = HomePageSearchBox(self.driver)
        search_box.click_one_way_flight()
        assert search_box.get_return_date() == DataSearchBox.ONE_WAY_DATE


if __name__ == '__main__':
    unittest.main(verbosity=2)


