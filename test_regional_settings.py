# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.regional_settings_box import RegionalSettingsBox
from data_test import DataRegionalSettings
from data_test import DataMainPage
import time


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
        home_page = HomePage(self.driver)
        home_page.click_regional_settings()

        regional_settings = RegionalSettingsBox(self.driver)
        regional_settings.click_switch_to_eng()
        regional_settings.save_settings()
        time.sleep(3)

        self.assertIn(DataMainPage.ENG_WEB_TITLE, self.driver.title)

    def test_change_country_currency(self):
        home_page = HomePage(self.driver)
        home_page.click_regional_settings()

        regional_settings = RegionalSettingsBox(self.driver)
        #
        regional_settings.set_region("Dania")
        time.sleep(1)
        regional_settings.save_settings()
        time.sleep(5)

        home_page = HomePage(self.driver)
        self.assertIn(home_page.get_currency(), 'kr. DKK')


if __name__ == '__main__':
    unittest.main(verbosity=2)
