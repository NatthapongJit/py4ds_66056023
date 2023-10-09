"""
Exercise 21 : Validate Date
"""
from src.ex20 import is_leap_year

def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    # from src.sol20 import is_leap_year

    # FIX : complete this
    if not (1 <= month <= 12):
        return False
    if is_leap_year(year) and month == 2 and day == 29:
        return True
    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False
    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False
    elif month == 2 and not (1 <= day <= 28):
        return False

    return True
