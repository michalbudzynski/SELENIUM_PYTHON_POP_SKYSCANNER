# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from locators import HomePageLocators, FlightSearchBox
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WSB_Testuje(BasePage):
    def get_knowledge(self):
        python = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='python']")))

        python.click()

    def meetup_info(self):
        info = self.driver.find_element(By.ID, "meetupInfo")
        info.click()

    def and_more(self):
        more = self.driver.find_element(By.TAG_NAME, "more")
        more.click()

class HomePage(BasePage):

    def click_login_button(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, HomePageLocators.LOGIN_BTN)))

        btn.click()


class HomePageSearchBox(BasePage):

    def click_return_flight(self):
        btn_return = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.CHECKBOX_FLY_RETURN)))

        btn_return.click()

    def click_one_way_flight(self):
        btn_one_way = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.CHECKBOX_FLY_ONE_WAY)))

        btn_one_way.click()

    def click_multicity_flight(self):
        btn_multicity = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.CHECKBOX_FLY_MULTI)))

        btn_multicity.click()

    def click_change_flight(self):
        change_flight_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.CHANGE_FLIGHT_BTN)))

        change_flight_btn.click()

    def set_destinantion(self, destination):
        dest_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.FLY_DESTINATION)))

        dest_field.click()
        dest_field.send_keys(destination)

    def set_orgin(self, origin):
        origin_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.FLY_ORIGIN)))

        origin_field.click()
        origin_field.send_keys(origin)

    def click_search_flight(self):
        btn_search = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.BTN_SEARCH)))

        btn_search.click()

    def get_departure_date(self):
        depart_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.DEPART_DATE)))

        return depart_date.text

    def get_return_date(self):
        return_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.RETURN_DATE)))

        return return_date.text

    def get_flight_validation_msg(self):
        msg = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.VALIDATION_MSG)))
        return msg.text

    def get_origin(self):
        origin_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.FLY_ORIGIN)))
        return origin_field.get_attribute("value")

    def get_destination(self):
        dest_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, FlightSearchBox.FLY_DESTINATION)))
        return dest_field.get_attribute("value")


