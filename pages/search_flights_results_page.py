import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SearchFlightResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver) # to instantiate BaseDriver class
        self.driver = driver

    # locators
    FILTER_BY_1_STOP_ICON= "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop')]"

    def get_filter_by_one_stop_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            print("Selected flights with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            print("Selected flights with 2 stops")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            print("Selected non stop flights")
            time.sleep(2)
        else:
            print("Please provide valid filter option")
