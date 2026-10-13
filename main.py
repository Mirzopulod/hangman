import random


def show_menu():
    print("\n=== Игра Виселица ===")
    print("Добро пожаловать в игру Hangman")
    print("1. Новая игра")
    print("0. Выход")


def show_begin():
    print("\n=== Запущено новая игра ===")
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


def get_situation(number_of_try):
    HANDMAN = [
        """
          _____
          |   |
              |
              |
              |
        ______|___
    """,
        """
          _____
          |   |
          0   |
              |
              |
        ______|___
    """,
        """
          _____
          |   |
          0   |
          |   |
              |
        ______|___
    """,
        """
          _____
          |   |
          0   |
         \|   |
              |
        ______|___
    """,
        """
          _____
          |   |
          0   |
         \|/  |
              |
        ______|___
    """,
        """
          _____
          |   |
          0   |
         \|/  |
         /    |
        ______|___
    """,
        """
          _____
          |   |
          0   |
         \|/  |
         / \  |
        ______|___
    """
    ]
    print(HANDMAN[number_of_try])


def try_stand(word):
    show_begin()

    number = 0
    player = []

    for i in range(len(word)):
        player.append('_')

    while number < 6:
        trying = False
        get_situation(number)

        for n in range(len(player)):
            print(player[n], end=" ")
        print()

        choise = get_choice()
        choise = try_choice(choise)

        for n in range(len(word)):
            if word[n] == choise:
                if player[n] == word[n]:
                    print("Это буква уже была записана")
                    trying = True
                    break
                player[n] = word[n]
                trying = True

        if not trying:
            number += 1
            print("Осторожно осталось попыток ", 6 - number)
        else:
            print("Верно! Продолжайте ")

        trying = False

        if word == player:
            print("Ура вы победили")
            break

    if number == 6:
        get_situation(number)
        print("Увы вы проиграли")


def main():
    while True:
        show_menu()
        myword = get_sample()
        choise = get_choice()

        if choise == '1':
            try_stand(myword)
        elif choise == '0':
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()