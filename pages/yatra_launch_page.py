import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from selenium.webdriver.common.keys import Keys
from pages.search_flights_results_page import SearchFlightResults


class LaunchPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flights']"

    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def get_going_to_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.GOING_TO_RESULT_LIST)

    def get_departure_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SELECT_DATE_FIELD)

    def get_all_dates_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def get_search_button(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BUTTON)

    def enter_depart_from_location(self, depart_location):
        self.get_depart_from_field().click()
        time.sleep(2)
        self.get_depart_from_field().send_keys(depart_location)
        self.get_depart_from_field().send_keys(Keys.ENTER)

    def enter_going_to_location(self, going_to_location):
        self.get_going_to_field().click()
        time.sleep(2)
        self.get_going_to_field().send_keys(going_to_location)
        search_results = self.get_going_to_results()
        # lopping over results and selecting location
        for results in search_results:
            if going_to_location in results.text:
                results.click()
                break

    def enter_departure_date(self, departure_date):
        self.get_departure_date_field().click()
        all_dates = self.get_all_dates_field().find_elements(By.XPATH, self.ALL_DATES)

        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                time.sleep(2)
                break

    def click_search_flight_button(self):
        self.get_search_button().click()
        time.sleep(2)

    def search_flights(self, departure_location, going_to_lctn, depart_date):
        self.enter_depart_from_location(departure_location)
        self.enter_going_to_location(going_to_lctn)
        self.enter_departure_date(depart_date)
        self.click_search_flight_button()

