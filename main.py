import random


def show_begin():
    print("\n=== Игра Виселица ===")
    print("Добро пожаловать в игру Hangman")
    print("Задано слово. Угадайте его")


def get_sample():
    words = ["яблоко", "школа", "турист", "ноутбук", "земля", "небо"]
    word = list(random.choice(words))
    return word


def get_choice():
    return input("Выбери букву: ").strip()


def try_choice(letter):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    while letter not in alphabet or len(letter) > 1:
        print("Пишите только 1 русскую букву:")
        letter = get_choice()
    return letter


def try_stand(word):
    number = 0
    player = []

    for i in range(len(word)):
        player.append('_')

    while number < 5:
        trying = False

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
            print("Осторожно осталось попыток ", 5 - number)
        else:
            print("Верно! Продолжайте ")

        trying = False

        if word == player:
            print("Ура вы победили")
            break

    if number == 5:
        print("Увы вы проиграли")


def main():
    myword = get_sample()
    show_begin()
    try_stand(myword)


if __name__ == "__main__":
    main()