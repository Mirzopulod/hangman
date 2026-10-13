import random

HANGMAN = [
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


def get_random_word():
    try:
        with open("words.txt", "r", encoding="utf-8") as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("Файл words.txt не найден")
        return None

    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    clean_words = []
    for w in words:
        if len(w) < 3:
            continue
        is_russian = True

        for ch in w:
            if ch not in alphabet:
                is_russian = False
                break
        if is_russian:
            clean_words.append(w)

    words = clean_words

    if not words:
        print("Словарь пуст")
        return None

    return list(random.choice(words))


def get_choice():
    return input("Напишите: ").strip()


def validate_letter(letter):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    while len(letter) != 1 or letter not in alphabet:
        print("Пишите только 1 русскую букву:")
        letter = get_choice()
    return letter


def show_hangman(errors):
    print(HANGMAN[errors])


def play_round(word):
    show_begin()

    errors = 0
    mask = ['_'] * len(word)
    used_letters = []

    show_hangman(errors)

    while errors < 6:
        found = False

        for n in range(len(mask)):
            print(mask[n], end=" ")
        print()

        choice = get_choice()
        choice = validate_letter(choice)

        if choice in used_letters:
            print("Это буква уже была введена")
            print("Введенные буквы: ", *used_letters)
            continue

        used_letters.append(choice)

        for n in range(len(word)):
            if word[n] == choice:
                mask[n] = word[n]
                found = True

        show_hangman(errors)

        if word == mask:
            print(*mask)
            print("Ура вы победили")
            break
        elif not found:
            errors += 1
            print("Осторожно осталось попыток ", 6 - errors)
        else:
            print("Верно! Продолжайте ")

        print("Введенные буквы: ", *used_letters)

    if errors == 6:
        show_hangman(errors)
        print("Увы вы проиграли")
        print("Слово было: ", *word, sep="")


def main():
    while True:
        show_menu()
        choice = get_choice()

        if choice == '1':
            myword = get_random_word()
            if myword is None:
                continue
            play_round(myword)
        elif choice == '0':
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()