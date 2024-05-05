import re

INITIAL_DELIMETERS = ["\n"]


def add(numbers: str) -> int:
    if len(numbers) == 0:
        return 0

    allowed_delimiters, sanitized_numbers = get_delimeters_and_sanitize_numbers(numbers)
    regex_pattern = "|".join(map(re.escape, allowed_delimiters))
    number_list = re.split(regex_pattern, sanitized_numbers)
    check_negative_numbers(number_list)

    return sum(map(lambda x: convert_str_to_number(x), number_list))


def get_delimeters_and_sanitize_numbers(numbers: str):
    allowed_delimiters = [*INITIAL_DELIMETERS]

    if not numbers.startswith("//"):
        allowed_delimiters.append(",")
        return allowed_delimiters, numbers

    regex_group = re.search("//(.*)\n", numbers)
    custom_delimeter = regex_group.group(1)
    replaced_string = re.sub("//(.*)\n", "", numbers)
    allowed_delimiters.append(custom_delimeter)

    return allowed_delimiters, replaced_string


def convert_str_to_number(x):
    try:
        return int(x)
    except:
        raise Exception("Invalid Number")


def check_negative_numbers(number_list):
    negative_numbers = [i for i in number_list if convert_str_to_number(i) < 0]
    if len(negative_numbers) == 0:
        return False

    raise Exception(f"negative numbers are not allowed {','.join(negative_numbers)}")
