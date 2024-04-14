from random import choice


def random_compliment(path_for_name: str = "../data/name",
                      path_for_complimentory: str = "../data/compliment") -> str:
    """проходится по файлам и возврошает случайное имя и комплимент"""
    with open(path_for_complimentory, "r", encoding="utf-8") as file:
        list_complimentory = []
        for line in file:
            list_complimentory.append(line.strip())
    with open(path_for_name, "r", encoding="utf8") as file:
        list_name = []
        for line in file:
            list_name.append(line.split()[0].strip())
    return f"{choice(list_name)} {choice(list_complimentory)}"


def random_phrases(path_for_phrases: str = "../data/phrases.txt") -> str:
    """берет случайную фразу"""
    with open(path_for_phrases, encoding="utf-8") as file:
        list_phrases = []
        for line in file:
            list_phrases.append(line.strip().split("\\n"))
    return "\n".join(choice(list_phrases))


def random_motivation(path_for_motivation: str = "../data/motivation.txt") -> str:
    with open(path_for_motivation, encoding="utf-8") as file:
        list_phrases = []
        for line in file:
            list_phrases.append(line.strip().split("\\n"))
    return "\n".join(choice(list_phrases))
