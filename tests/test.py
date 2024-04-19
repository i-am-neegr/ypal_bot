from src.choise_text import (random_compliment, random_motivation_morning, random_motivation_evening,
                             random_phrases)
import random

print(random_compliment())
print()
print(random_phrases())
print()
test = [random_compliment, random_phrases, random_motivation_morning, random_motivation_evening]


for _ in range(500):
    f = random.choice(test)
    print(f())
    print()

