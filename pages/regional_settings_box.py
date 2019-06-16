# -*- coding: utf-8 -*-

from pages.base_page import BasePage
from locators import RegionalSettingsLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RegionalSettingsBox(BasePage):

    def click_switch_to_eng(self):
        switch_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.SWITCH_ENG)))

        switch_btn.click()

    def get_language(self):
        lang = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.LANG)))

        return lang.get_attribute("value")

    def set_language(self, language):
        lang = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.LANG)))

        lang.click()
        lang.select_by_visible_text(language)

    def get_region(self):
        region = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.REGION)))

        return region.get_attribute("value")

    def set_region(self, region):
        reg = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.REGION)))

        reg.click()
        select = Select(reg)

        # select by visible text
        select.select_by_visible_text(region)

        reg.click()

    def get_currency(self):
        currency = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.CURRENCY)))

        return currency.get_attribute("value")

    def set_currency(self, currency):
        curr = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.CURRENCY)))

        curr.click()
        curr.select_by_visible_text(currency)

    def close_box(self):
        close_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.CLOSE)))

        close_btn.click()

    def get_box_header(self):
        box_header = self.driver.find_element(By.ID, RegionalSettingsLocators.HEADER_INFO)

        return box_header.text

    def save_settings(self):
        save_btn = self.driver.find_element(By.ID, RegionalSettingsLocators.SAVE_BTN)

        save_btn.click()

