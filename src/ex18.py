def get_cost_of_coffee(number_of_coffees, price_per_coffee):
    """
    Calculate the total cost of buying a number of coffees,
    with a promotion "buy 8 get 1 free".

    Args:
        number_of_coffees (int): The total number of coffees to buy.
        price_per_coffee (float): The cost of one cup of coffee.

    Returns:
        float: The total cost of buying the given number of coffees with the promotion.
    """

    # Track the total price:
    total_price = 0.0

    cups_until_free_coffee = 8

    while number_of_coffees > 0:

        number_of_coffees -= 1

        if cups_until_free_coffee == 0:
            cups_until_free_coffee = 8
        else:
            total_price += price_per_coffee
            cups_until_free_coffee -= 1
    return total_price
def get_cost_of_coffee_2(number_of_coffees, price_per_coffee):
    """
    Calculate the total cost of buying a number of coffees,
    with a promotion "buy 8 get 1 free".

    Args:
        number_of_coffees (int): The total number of coffees to buy.
        price_per_coffee (float): The cost of one cup of coffee.

    Returns:
        float: The total cost of buying the given number of coffees with the promotion.
    """

    # Track the total price:
    total_price = 0.0

    cups_until_free_coffee = 8

    while number_of_coffees > 0:

        number_of_coffees -= 1

        if cups_until_free_coffee == 0:
            cups_until_free_coffee = 8
        else:
            total_price += price_per_coffee
            cups_until_free_coffee -= 1
    return total_price