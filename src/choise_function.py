from random import choice
from src.choise_text import random_motivation, random_phrases, random_compliment


def random_function(list_function: list) -> str:
    """берет рандом """
    function = choice(list_function)
    return function()
