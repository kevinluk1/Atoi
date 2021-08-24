import unittest
import random

from atoi import conv_num, helper_is_valid_hex, helper_is_valid_negative


class TestCase(unittest.TestCase):

    def test_return_none_if_empty_1(self):
        self.assertEqual(conv_num(''), None)

    def test_return_none_if_empty_2(self):
        self.assertEqual(conv_num(' '), None)

    def test_return_false_if_invalid(self):
        self.assertIsNone(conv_num('*'))

    def test_return_false_if_invalid_beginning_1(self):
        self.assertIsNone(conv_num('-'))

    def test_return_false_if_invalid_beginning_2(self):
        self.assertIsNone(conv_num('.'))

    def test_return_positive_number_1(self):
        self.assertEqual(conv_num('2'), 2)

    def test_return_positive_number_2(self):
        self.assertEqual(conv_num('500'), 500)

    def test_return_negative_number(self):
        self.assertEqual(conv_num("-500"), -500)

    def test_return_negative_number_2(self):
        self.assertEqual(conv_num("-1"), -1)

    def test_return_negative_number_3(self):
        self.assertEqual(conv_num("-1.0"), -1.0)

    def test_return_negative_number_4(self):
        self.assertEqual(conv_num("-.10"), -.10)

    def test_minus_invalid_placement_1(self) -> None:
        self.assertIsNone(conv_num("10-1"))

    def test_symbols_1(self):
        self.assertIsNone(conv_num("4^2"))

    def test_symbols_2(self):
        self.assertIsNone(conv_num(".1%"))

    def test_minus_invalid_placement_2(self) -> None:
        self.assertIsNone(conv_num("132032-1"))

    def test_return_float_1(self):
        self.assertEqual(conv_num(".123"), .123)

    def test_return_float_2(self):
        self.assertEqual(conv_num(".439850398523"), .439850398523)

    def test_return_float_3(self):
        self.assertEqual(conv_num("1.0"), 1.0)

    def test_return_float_4(self):
        self.assertEqual(conv_num("-123.45"), -123.45)

    def test_return_float_5(self):
        self.assertEqual(conv_num("-.45"), -0.45)

    def test_return_float_6(self):
        self.assertEqual(conv_num("123."), 123.0)

    def test_multiple_decimals(self):
        self.assertFalse(conv_num("1.1.1"))

    def test_return_negative(self):
        self.assertEqual(conv_num('-12345'), -12345)

    def test_type(self):
        self.assertTrue(type(conv_num(".1")), float)

    def test_is_valid_negative_1(self):
        self.assertTrue(helper_is_valid_negative("-1"))

    def test_is_valid_negative_2(self):
        self.assertFalse(helper_is_valid_negative("1-"))

    def test_is_valid_negative_3(self):
        self.assertFalse(helper_is_valid_negative('-'))

    def test_is_valid_negative_4(self):
        self.assertFalse(helper_is_valid_negative('1'))

    def test_reject_invalid_hex_prefix_1(self):
        self.assertFalse(helper_is_valid_hex("1x"))

    def test_accept_valid_hex_prefix_1(self):
        self.assertTrue(helper_is_valid_hex("0x"))

    def test_accept_valid_hex_prefix_2(self):
        self.assertTrue(helper_is_valid_hex("-0x"))

    def test_reject_invalid_hex_prefix_2(self):
        self.assertFalse(helper_is_valid_hex("-1x"))

    def test_rec_calculate_hex_1(self):
        self.assertEqual(conv_num("0x55"), 85)

    def test_rec_calculate_hex_2(self):
        self.assertEqual(conv_num("0x100"), 256)

    def test_rec_calculate_hex_3(self):
        self.assertEqual(conv_num("0x5E"), 94)

    def test_rec_calculate_hex_4(self):
        self.assertEqual(conv_num("0xDEADBEEF"), 3735928559)

    def test_rec_calculate_hex_5(self):
        self.assertEqual(conv_num("0Xdeadbeef"), 3735928559)

    def test_rec_calculate_hex_6(self):
        self.assertEqual(conv_num("-0XAD4"), -2772)

    def test_rec_calculate_hex_7(self):
        self.assertIsNone(conv_num("XXAD4"), 2772)

    def test_rec_calculate_hex_8(self):
        self.assertIsNone(conv_num("0X DEA"))

    def test_reject_spaces(self):
        self.assertIsNone(conv_num("-. 34"))