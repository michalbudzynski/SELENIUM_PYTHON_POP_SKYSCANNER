# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_box import LoginBox
from data_test import DataLoginBox
from time import sleep


class LoginToSite(unittest.TestCase):
    def setUp(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.maximize_window()
        self.driver.get("https://skyscanner.pl/")

    def tearDown(self):

        self.driver.quit()

    def test_incorrect_login_msg(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()

        login_box = LoginBox(self.driver)
        login_box.click_login_by_email()
        login_box.set_incorrect_email()
        login_box.click_password_field()
        assert DataLoginBox.EMAIL_VALIDATE_MSG == login_box.get_email_validation_msg()

    def test_empty_login_msg(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()

        login_box = LoginBox(self.driver)
        login_box.click_login_by_email()
        login_box.click_email_field()
        login_box.click_password_field()
        assert DataLoginBox.EMPTY_LOGIN_MSG == login_box.get_email_validation_msg()

    def test_empty_password_msg(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()

        login_box = LoginBox(self.driver)
        login_box.click_login_by_email()
        login_box.set_email()
        login_box.click_password_field()
        login_box.click_email_field()
        assert DataLoginBox.EMPTY_PASSWORD_MSG == login_box.get_password_validation_msg()

    def test_reset_password_validation_msg(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()

        login_box = LoginBox(self.driver)
        login_box.click_login_by_email()
        login_box.click_reset_password()
        assert DataLoginBox.EMPTY_LOGIN_MSG == login_box.get_email_validation_msg()

    def test_strong_password_validation(self):
        home_page = HomePage(self.driver)
        home_page.click_login_button()

        login_box = LoginBox(self.driver)
        login_box.click_login_by_email()
        login_box.click_register_account()
        sleep(2)
        login_box.set_email()
        login_box.click_submit_button()
        login_box.click_password_field()
        login_box.set_password("123")
        # number - At least one number, min_char - 8 or more characters, upper_lower - Uppercase and lowercase letters
        login_box.check_strong_password("number")
        login_box.set_password("45678$%")
        login_box.check_strong_password("min_char")
        login_box.set_password("mB")
        login_box.check_strong_password("upper_lower")


if __name__ == '__main__':
    unittest.main(verbosity=2)