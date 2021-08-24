import random
import string


def hex_rng(valid=True):
    hex_string_suffix = ""
    acceptable = "ABCDEF123456789abcdef"
    possible_prefix_list = ["0x", "0X"]
    impossible_prefix_list = [str(random.randint(0, 9)), random.choice(
        string.ascii_letters), " "]

    for i in range(random.randint(2, 5)):
        if valid is True:
            prefix = random.choice(possible_prefix_list)
            hex_string_suffix = hex_string_suffix + ''.join(
                random.choice(acceptable))

        if valid is False:
            z = [possible_prefix_list, impossible_prefix_list]
            prefix_pre = random.choice(z)
            prefix = random.choice(prefix_pre)

            suffix = random.choice([string.ascii_letters, string.digits,
                                    string.printable])
            hex_string_suffix = hex_string_suffix + ''.join(
                random.choice(suffix))

    return str(prefix + hex_string_suffix)