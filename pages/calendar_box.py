# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from locators import HomePageLocators, FlightSearchBox
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalendarBox(BasePage):
    def set_month(self, month):
        pass

    def set_day(self, day):
        pass

    def set_date(self, day, month, year):
        pass

    def click_whole_month(self):
        pass

    def click_specific_date(self):
        pass

    def click_next_months(self):
        pass

    def click_previous_month(self):
        pass
