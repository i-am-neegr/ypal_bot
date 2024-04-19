from random import choice


def random_compliment(path_for_name: str = "C:\\Users\\Student Free\\PycharmProjects\\ypal_bot1\\data\\name.txt",
                      path_for_complimentory: str = "C:\\Users\\Student Free\\PycharmProjects\\ypal_bot1\\data\\compliment.txt") -> str:
    """проходится по файлам и возврошает случайное имя и комплимент"""
    with open(path_for_complimentory, "r", encoding="utf-8") as file:
        list_complimentory = []
        for line in file:
            list_complimentory.append(line.rstrip())
    with open(path_for_name, "r", encoding="utf8") as file:
        list_name = []
        for line in file:
            list_name.append(line.split()[0].strip())
    return f"{choice(list_name)}{choice(list_complimentory)}"


def random_phrases(
        path_for_phrases: str = "C:\\Users\\Student Free\\PycharmProjects\\ypal_bot1\\data\\phrases.txt") -> str:
    """берет случайную фразу"""
    with open(path_for_phrases, encoding="utf-8") as file:
        list_phrases = []
        for line in file:
            list_phrases.append(line.strip().split("\\n"))
    return "\n".join(choice(list_phrases))


def random_motivation_morning(
        path_for_motivation_morning: str = "C:\\Users\\Student Free\\PycharmProjects\\ypal_bot1\\data\\morning_mot.txt") -> str:
    """берет случайную утреннию фразу"""
    with open(path_for_motivation_morning, encoding="utf-8") as file:
        list_phrases = []
        for line in file:
            list_phrases.append(line.strip().split("\\n"))
    return "\n".join(choice(list_phrases))


def random_motivation_evening(
        path_for_motivation_evening: str = "C:\\Users\\Student Free\\PycharmProjects\\ypal_bot1\\data\\evening_mot.txt") -> str:
    """берет случайную вечернию фразу"""
    with open(path_for_motivation_evening, encoding="utf-8") as file:
        list_phrases = []
        for line in file:
            list_phrases.append(line.strip().split("\\n"))
    return "\n".join(choice(list_phrases))
