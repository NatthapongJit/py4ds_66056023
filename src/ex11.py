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
    if tsec == 0:
        return '0s'
    totalSeconds = tsec
    if totalSeconds >= 3600:
        hours = totalSeconds // 3600
        totalSeconds = totalSeconds % 3600
    else:
        hours = 0
    if totalSeconds >= 60:
        minutes = totalSeconds // 60
        totalSeconds = totalSeconds % 60
    else:
        minutes = 0
    seconds = totalSeconds
    hms = []
    if hours > 0:
        hms.append(str(hours) + 'h')

    if minutes > 0:
        hms.append(str(minutes) + 'm')

    if seconds > 0:
        hms.append(str(seconds) + 's')
    return ' '.join(hms)
