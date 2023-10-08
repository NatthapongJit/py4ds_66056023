"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    tt = tsec
    if tt == 0:
        return '0s'
    if tt >= 3600:
        h = tt // 3600
        tt = tt % 3600
    else:
        h = 0
    if tt >= 60:
        min = tt // 60
        tt = tt % 60
    else:
        min = 0
    sec = tt
    hms = []
    if h > 0:
        hms.append(str(h) + 'h')

    if min > 0:
        hms.append(str(min) + 'm')

    if sec > 0:
        hms.append(str(sec) + 's')
    return ' '.join(hms)
