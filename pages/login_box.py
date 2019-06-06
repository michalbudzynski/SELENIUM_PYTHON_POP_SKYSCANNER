# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from locators import LoginBoxLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data_test import DataLoginBox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginBox(BasePage):
    def click_login_by_email(self):
        email_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.LOGIN_BY_MAIL_BUTTON)))

        email_btn.click()

    def click_submit_button(self):
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.SUBMIT_BUTTON)))

        submit_btn.click()

    def set_incorrect_email(self):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.EMAIL_FIELD)))

        email_field.click()
        email_field.send_keys(DataLoginBox.INCORRECT_MAIL)

    def set_password(self):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.PASSWORD_FIELD)))

        password_field.click()
        password_field.send_keys("123")

    def get_email_validation_msg(self):
        email_validate_msg = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.EMAIL_VALIDATE_BOX)))
        return email_validate_msg.text

    def get_password_validation_msg(self):
        password_validate_msg = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.PASSWORD_VALIDATE_BOX)))
        return password_validate_msg.text

    def click_register_account(self):
        register_btn = self.driver.find_element(By.XPATH, LoginBoxLocators.SUBMIT_BUTTON)
        register_btn.click()

    def set_email(self):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.EMAIL_FIELD)))

        email_field.click()
        email_field.send_keys(DataLoginBox.CORRECT_EMAIL)

    def click_email_field(self):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.EMAIL_FIELD)))

        email_field.click()

    def click_password_field(self):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginBoxLocators.PASSWORD_FIELD)))

        password_field.click()

    def click_reset_password(self):
        reset_password = self.driver.find_element(By.ID, LoginBoxLocators.RESET_PASSWORD_BTN)

        reset_password.click()

