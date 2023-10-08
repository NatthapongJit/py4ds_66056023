"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # FIX : complete this
    # * If the last two digits end with 11, 12, or 13 then the suffix is ―th.
    # * If the number ends with 1, the suffix is ―st.
    # * If the number ends with 2, the suffix is ―nd.
    # * If the number ends with 3, the suffix is ―rd.
    # * Every other number has a suffix of ―th.
    if num % 100 == 11 or num % 100 == 12 or num % 100 == 13:
        return str(num)+'th'
    elif num % 10 == 1 :
        return str(num)+'st'
    elif num % 10 == 2 :
        return str(num)+'nd'
    elif num % 10 == 3 :
        return str(num)+'rd'
    else :
        return str(num)+'th'



