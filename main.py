import random

HANDMAN = [
    r"""
        _____
        |   |
            |
            |
            |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
            |
            |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
        |   |
            |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
       \|   |
            |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
       \|/  |
            |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
       \|/  |
       /    |
      ______|___
""",
    r"""
        _____
        |   |
        0   |
       \|/  |
       / \  |
      ______|___
"""
]


def show_menu():
    print("\n=== Игра Виселица ===")
    print("Добро пожаловать в игру Hangman")
    print("1. Новая игра")
    print("0. Выход")


def show_begin():
    print("\n=== Запущена новая игра ===")
    print("Задано слово. Угадайте его")


def get_sample():
    with open("words.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
    return list(random.choice(words))


def get_choice():
    return input("Напишите: ").strip()


def try_choice(letter):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    while letter not in alphabet or len(letter) > 1:
        print("Пишите только 1 русскую букву:")
        letter = get_choice()
    return letter


def show_hangman(errors_of_try):
    print(HANDMAN[errors_of_try])


def play_round(word):
    show_begin()

    errors = 0
    mask = ['_'] * len(word)
    used_letters = set()

    while errors < 6:
        found = False
        show_hangman(errors)

        for n in range(len(mask)):
            print(mask[n], end=" ")
        print()

        choice = get_choice()
        choice = try_choice(choice)

        if choice in used_letters:
            print("Это буква уже была введена")
            continue

        used_letters.add(choice)

        for n in range(len(word)):
            if word[n] == choice:
                mask[n] = word[n]
                found = True

        if word == mask:
            print("Ура вы победили")
            break
        elif not found:
            errors += 1
            print("Осторожно осталось попыток ", 6 - errors)
        else:
            print("Верно! Продолжайте ")

    if errors == 6:
        show_hangman(errors)
        print("Увы вы проиграли")
        print("Слово было: ", *word, sep="")


def main():
    while True:
        show_menu()
        choice = get_choice()

        if choice == '1':
            myword = get_sample()
            play_round(myword)
        elif choice == '0':
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()