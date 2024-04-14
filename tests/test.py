from src.choise_text import random_compliment, random_phrases, random_motivation
from src.choise_function import random_function

# print(random_compliment())
# print()
# print(random_phrases())
# print()
# print(random_motivation())
test = [random_compliment, random_phrases, random_motivation]

for _ in range(50):
    print(random_function(test))
    print()
