from selenium.webdriver.common.by import By

# home_page_locators


class HomePageLocators(object):

    LOGIN_BTN = "//span[@class='login']"

    SETTINGS_BTN = "//*[@id='culture-info']/button"

    CURRENCY = "//*[@class='CultureSelectorButton_CultureSelectorButton__currency-label__2NkFI']"

        #"//li[@id='culture-info']/button//span"


class FlightSearchBox(object):

    FLY_DESTINATION = "//input[@name='fsc-destination-search']"

    FLY_ORIGIN = "//input[@name='fsc-origin-search']"

    CHECKBOX_FLY_ONE_WAY = "//input[@id='fsc-trip-type-selector-one-way']"

    CHECKBOX_FLY_RETURN = "//input[@id='fsc-trip-type-selector-return']"

    CHECKBOX_FLY_MULTI = "//input[@id='fsc-trip-type-selector-multi-destination']"

    DEPART_DATE = "//button[@id='depart-fsc-datepicker-button']"

    RETURN_DATE = "//button[@id='return-fsc-datepicker-button']"

    VALIDATION_MSG = "//div[@class='App_fsc-form-validation__1Zmzp']"

    CHANGE_FLIGHT_BTN = "//button[@class='SwitchButton_SwitchButton__button__b_XwX']"

    BTN_SEARCH = "//button[@type='submit']"


class LoginBoxLocators(object):

    LOGIN_BY_MAIL_BUTTON = "//div[@data-testid='login-email-button']"

    EMAIL_FIELD = "//input[@type='email']"

    PASSWORD_FIELD = "//input[@type='password']"

    LOGIN_BUTTON = "//button[@data-testid='login-button']"

    ALERT_BOX = "//header[@role='alert']"

    REGISTER_BUTTON = "//button[@data-testid='login-signup-toggle-button']"

    SUBMIT_BUTTON = "//button[@data-testid='login-button']"

    EMAIL_VALIDATE_BOX = "//div[@id='email_validation_message']"

    PASSWORD_VALIDATE_BOX = "//div[@id='password_validation_message']"

    RESET_PASSWORD_BTN = "resetPasswordButton"


class CalendarBoxLocators(object):

    MONTHS = "//select[@name='months']"

    DAYS = "//tbody"


class RegionalSettingsLocators(object):

    SWITCH_ENG = "culture-selector-switch-to-english"

    LANG = "culture-selector-locale"

    REGION = "culture-selector-market"

    CURRENCY = "culture-selector-currency"

    SAVE_BTN = "culture-selector-save"

    CANCEL_BTN = "culture-selector-cancel"

    CLOSE = "//button[@title='Zamknij']"

    HEADER_INFO = "bpk-modal-heading-culture-selector-modal"


