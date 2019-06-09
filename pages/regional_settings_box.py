# -*- coding: utf-8 -*-

from pages.base_page import BasePage
from locators import RegionalSettingsLocators


class RegionalSettings(BasePage):

    def click_switch_to_eng(self):
        SWITCH_BTN = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, RegionalSettingsLocators.SWITCH_ENG)))

        SWITCH_BTN.click()

    def get_language(self):
        pass

    def set_language(self, lang):
        pass

    def get_region(self):
        pass

    def set_region(self, region):
        pass

    def get_currency(self):
        pass

    def set_currency(self, currency):
        pass

    def close_box(self):
        pass

