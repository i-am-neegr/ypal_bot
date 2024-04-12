from random import choice


def random_compliment(path_for_name: str = "../data/name",
                      path_for_complimentory: str = "../data/compliment") -> tuple[str, str]:
    """проходится по файлам и возврошает случайное имя и комплимент"""
    with open(path_for_complimentory, "r", encoding="utf-8") as file:
        list_complimentory = []
        for line in file:
            list_complimentory.append(line.strip())
    with open(path_for_name, "r", encoding="utf8") as file:
        list_name = []
        for line in file:
            list_name.append(line.split()[0].strip())
    return choice(list_name), choice(list_complimentory)
