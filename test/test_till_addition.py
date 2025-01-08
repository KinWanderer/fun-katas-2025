from src.till_addition import end_of_day

""" till_addition({ "1p": 1, "2p": 1 }
# should return "£0.03"

till_addition({ "1p": 1, "2p": 1, "5p": 1, "10p": 1, "20p": 1 })
# should return "£0.38"

till_addition({ "5p": 1, "10p": 1, "20p": 1, "50p": 1, "£1": 1 })
# should return "£1.85" """

class TestEndOfDay():
    def test_till_addition_small(self):
        assert end_of_day({ "1p": 1, "2p": 1 }) == "£0.03"
        assert end_of_day({ "1p": 1, "2p": 1, "5p": 1, "10p": 1, "20p": 1 }) == "£0.38"
        assert end_of_day({ "5p": 1, "10p": 1, "20p": 1, "50p": 1, "£1": 1 }) == "£1.85"

    def test_till_addition_large(self):
        assert end_of_day({"£20": 4, "£5": 1}) == "£85.00"
        assert end_of_day({"£10": 11, "£50": 1}) == "£160.00"

    def test_unepected_item_in_bagging_area(self):
        assert end_of_day({"p1": 55}) == "£0.00"
        assert end_of_day({}) == "£0.00"
        