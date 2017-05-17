import unittest


def encode(string: str) -> str:
    # TODO
    pass


def decode(string: str) -> str:
    # TODO
    pass


class TestEncoding(unittest.TestCase):
    def test_given(self):
        strings = {
            '0DE9MDK9J8I1BMUQ18HARUPOKXFE4HLADWV12OYYTUFI59Y1', # 47
            '6QXXCOLMUNBLYY0WOB5BR2HIR5L5XG02TGRAGV', # 36
            '5PNL', # 4
            'GKF8ANZ2DH6P3B5WWFMELX8XEMRSJGKHMDN932EZTM2O', # 43
            '4ZILNB9DW3Y65GIG4Z5WWICIJN6H7HTU88', # 32
            'Aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa', # 12
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW' # 14
        }

        for string in strings:
            assert decode(encode(string)) == string


if __name__ == '__main__':
    unittest.main()
