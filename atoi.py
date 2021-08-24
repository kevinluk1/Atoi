def conv_num(num_str) -> int or float or None:
    valid_ascii_values = [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
    float_present = False
    is_negative_float = False
    is_negative_hex = False
    is_hex = False

    if helper_is_valid_hex(num_str):
        is_hex = True

    if not is_hex:
        return int_or_float_to_string(num_str, valid_ascii_values,
                                      float_present, is_negative_float,
                                      is_negative_hex)
    if is_hex:
        if helper_is_valid_negative(num_str):
            is_negative_hex = True
        if not is_negative_hex:
            return rec_calculate_hex_to_deci(num_str, is_negative_float,
                                             is_negative_hex)
        if is_negative_hex:
            return (rec_calculate_hex_to_deci(num_str, is_negative_float,
                                              is_negative_hex
                                              )) * -1


def int_or_float_to_string(num_str, valid_ascii_values, float_present,
                           is_negative, is_negative_hex):
    if not helper_is_valid_number(num_str, valid_ascii_values):
        return None
    if helper_is_valid_negative(num_str) is True:
        is_negative = True
    if helper_is_valid_negative(num_str) is None:  # out of place '-'
        return None
    if helper_is_valid_float(num_str,
                             valid_ascii_values) is True:  # exactly 1 decimal
        float_present = True
    if helper_is_valid_float(num_str, valid_ascii_values) is None:
        # more than 1 decimal
        return None
    if float_present is False:
        string_to_int_value = helper_calculate_without_float(num_str,
                                                             is_negative,
                                                             is_negative_hex)
        return string_to_int_value
    if float_present is True:
        string_to_int_value = helper_calculate_with_float(num_str,
                                                          is_negative,
                                                          is_negative_hex)
        return string_to_int_value


def helper_is_valid_negative(num_str):
    """Function 1 helper method"""
    if len(num_str) == 1 and num_str[0] == '-':
        return False
    for i in range(1, len(num_str)):
        if ord(num_str[i]) == 45:
            return None
    if ord(num_str[0]) == 45:
        return True
    else:
        return False


def helper_is_valid_number(num_str, valid_ascii_codes):
    """Function 1 helper method"""
    if not num_str:
        return None

    if len(num_str) == 1 and ord(num_str[0]) in [45, 46]:
        return False

    for i in range(len(num_str)):
        if ord(num_str[i]) not in valid_ascii_codes:
            return False
    else:
        return True


def helper_find_decimal_index(num_str):
    """Function 1 helper method"""
    dec_location = 1
    counter = 0

    for i in range(len(num_str)):
        if num_str[i] == '.':
            counter += 1
            dec_location = i
    if counter > 1:
        return -2
    if counter == 0:
        return -1
    else:
        return dec_location + 1


def helper_is_valid_float(num_str, valid_ascii_codes):
    """Function 1 helper method"""
    for i in range(len(num_str)):
        if ord(num_str[i]) in valid_ascii_codes:
            decimal_location = helper_find_decimal_index(num_str)

        if decimal_location >= 0:  # if exactly 1 decimal
            return True

        if decimal_location == -1:  # if no decimals
            return False

        if decimal_location != -2:  # if more than one decimal
            return None


def helper_calculate_without_float(num_str, is_negative_float,
                                   is_negative_hex):
    """Function 1 helper method"""
    ascii_to_deci = 0

    for i in range(len(num_str)):
        if is_negative_float:
            if i == 0:
                continue
        ascii_to_deci = (ascii_to_deci * 10 + ord(num_str[i]) - 48)

    if not is_negative_float:
        return ascii_to_deci
    if is_negative_float:
        return ascii_to_deci*-1


def helper_calculate_with_float(num_str, is_negative, is_negative_hex):
    """Function 1 helper method"""
    ascii_to_deci = 0
    for i in range(len(num_str)):
        decimal_location = helper_find_decimal_index(num_str)
        if decimal_location == -1:
            return None
        if i == decimal_location - 1:
            continue

        if is_negative:  # skip '-'
            if i == 0:
                continue

        ascii_to_deci = (ascii_to_deci * 10 + ord(num_str[i]) - 48)
        if i == len(num_str) - 1:
            if not is_negative:
                return ascii_to_deci / 10 ** (
                        len(num_str) - decimal_location)
            if is_negative:
                return (ascii_to_deci / 10 ** (len(num_str) -
                                               decimal_location)) * -1

    return ascii_to_deci


def rec_calculate_hex_to_deci(num_str, is_negative, is_negative_hex):
    hex_dict = {"A": 10,
                "B": 11,
                "C": 12,
                "D": 13,
                "E": 14,
                "F": 15, }

    return_sum = 0
    counter1 = len(num_str) - 1

    if num_str == "0x" or num_str == "0X":
        return None
    if num_str[0] != "-":
        counter2 = 2
    if num_str[0] == "-":
        counter2 = 3

    offset = counter2

    return helper_calculate_hex_to_deci(num_str, counter1, counter2,
                                        return_sum, hex_dict, is_negative,
                                        offset, is_negative_hex)


def helper_calculate_hex_to_deci(num_str, counter1, counter2, return_sum,
                                 hex_dict, is_negative, offset,
                                 is_negative_hex):
    """Function 1 helper method"""
    if counter2 == len(num_str):
        return return_sum

    if 48 <= ord(num_str[counter1]) <= 57:  # if current iteration is a number
        deci_value = helper_calculate_without_float(num_str[counter1],
                                                    is_negative,
                                                    is_negative_hex)
    if 65 <= ord(num_str[counter1].upper()) <= 70:  # if current iteration is
        # ABCDEF
        deci_value = hex_dict[num_str[counter1].upper()]

    if ord(num_str[counter1]) == 32:  # if current iteration is blank
        return None

    if ord(num_str[counter1].upper()) not in range(48, 58) \
            and ord(num_str[counter1].upper()) not in range(65, 71):
        # range is non-inclusive of second parameter
        # if current iteration is neither ABCDEF or a character
        return None

    return_sum += deci_value * 16 ** (counter2 - offset)

    counter2 += 1
    counter1 -= 1

    return helper_calculate_hex_to_deci(num_str, counter1, counter2,
                                        return_sum, hex_dict, is_negative,
                                        offset, is_negative_hex)


def helper_is_valid_hex(num_str):
    """Function 1 helper method"""
    if not num_str:
        return None

    if not helper_is_valid_negative(num_str):
        if num_str[0] != '0' or num_str[1].lower() != 'x':
            return False
        else:
            return True
    if helper_is_valid_negative(num_str):
        if num_str[1] != '0' or num_str[2].lower() != 'x':
            return False
        else:
            return True