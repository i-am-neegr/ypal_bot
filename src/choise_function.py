from random import choice

from src.choise_text import (random_compliment, random_motivation,
                             random_phrases)


def random_function(list_function: list) -> str:
    """берет рандом """
    function = choice(list_function)
    return function()
