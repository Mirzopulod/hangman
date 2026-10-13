print("Добро пожаловать в игру Hangman")
print("Задано слово. Угадайте его")
word = ['я','б','л','о','к','о']

player = ['_','_','_','_','_','_']

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

number = 0

trying = False

  
def trying1():

    t9 = input()

    while t9 not in alphabet or len(t9) > 1:

            print("Пишите только 1 русскую букву:")

            t9 = input()

    return t9
  

while number < 5:

    for n in range(len(player)):

        print(player[n], end = " ")

    print()

    t9 = trying1()

    for n in range(len(word)):

        if(word[n] == t9):

            if(player[n] == word[n]):

                print("Это буква уже была записана")

                trying = True

                break

            player[n] = word[n]

            trying = True

    if( not trying):

        number += 1

        print("Осторожно осталось попыток ", 5 - number)

    else:

        print("Верно! Продолжайте ")

    trying = False


    if (word == player):

        print("Ура вы победили")

        break

if (number == 5):

    print("Увы вы проиграли")