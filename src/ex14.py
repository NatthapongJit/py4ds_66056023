"""
Exercise 14
"""

def average(num_list: list):
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    if len(num_list) == 0:
        return 0.0
    total = 0.0
    for number in num_list:
        total += number
    return total / len(num_list)
