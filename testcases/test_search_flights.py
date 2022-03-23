import pytest
import time
from selenium.webdriver.common.by import By
from pages.yatra_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResults
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):

        lp = LaunchPage(self.driver) # object of LaunchPage class

        lp.search_flights("New Delhi", "New York", "24/08/2022")
        # search_results_object = lp.search_flights("New Delhi", "New York", "24/08/2022")

        # to handle dynamic scroll
        lp.page_scroll()

        # Filter flights by 1 stop
        sf = SearchFlightResults(self.driver)
        sf.filter_flights_by_stop("1 Stop")  # filtering flights by requested stop

        all_stops = sf.get_search_flight_results()
        print(len(all_stops))

        # Verify that filtered results show flights having only 1 stop
        ut = Utils()
        ut.assert_list_item_text(all_stops, "1 Stop")


