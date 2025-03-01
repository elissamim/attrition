import re

def keep_only_digits(s:str)->str:
    """
    Keeps only characters that are digits in a string.

    Args:
        s (str): The string to modify.

    Returns:
        str: A string containing only digits.
    """
    return re.sub(r"\D", "", s)