"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""

def bottles_of_beer(bottle):
    """
    Calculate the number of bottles of beer on the wall.
    Returns the lyrics for each number of bottles.

    Parameters:
        bottle (int): The number of bottles of beer on the wall.

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # Singular or plural form of 'bottle'
    bottle_word = "bottle" if bottle == 1 else "bottles"

    # Construct the lyrics
    l = f"{bottle} {bottle_word} of beer on the wall,\n"
    l += f"{bottle} {bottle_word} of beer.\n"
    l += f"Take one down, pass it around,\n"

    # Adjust for last bottle
    if bottle - 1 == 0:
        l += "No more bottles of beer on the wall!\n"
    else:
        next_bottle_word = "bottle" if bottle - 1 == 1 else "bottles"
        l += f"{bottle - 1} {next_bottle_word} of beer on the wall.\n"

    return l


def loop_bottles_of_beers(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_beers(99)
