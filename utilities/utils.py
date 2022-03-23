
class Utils:

    def assert_list_item_text(self, list_of_elem, value):

        for stop in list_of_elem:
            print("The text is: " + stop.text)
            assert stop.text == value
            print('assert pass')