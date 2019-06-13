# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.regional_settings_box import RegionalSettingsBox
from data_test import DataRegionalSettings
from data_test import DataSearchBox


class RegionalSettings(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://skyscanner.pl/")

    def tearDown(self):

        self.driver.quit()

    def test_switch_to_eng_box_header(self):
        home_page = HomePage(self.driver)
        home_page.click_regional_settings()

        regional_settings = RegionalSettingsBox(self.driver)
        regional_settings.click_switch_to_eng()
        assert regional_settings.get_box_header() == DataRegionalSettings.HEADER

    def test_switch_to_eng_page_title(self):
        pass

    def test_change_country_currency(self):
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
