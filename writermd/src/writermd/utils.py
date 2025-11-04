
def kebab_case(s: str) -> str:
    """Converts a string to kebab-case.

    :param s: Input string.
    :return: Kebab-case string.
    """
    return s.replace(" ", "-").lower()
