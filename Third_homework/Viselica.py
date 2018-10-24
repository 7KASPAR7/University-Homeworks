import random


def game():
    count = 5
    secret_word = nachalo()
    result = shifrovka(secret_word)
    guessing(count, secret_word, result)


def guessing(count, secret_word, result):
    k = 0
    used_letters = []
    while count > 0 and k != len(secret_word):
        print('Попыток', count)
        letter = str(input('Введите букву'))
        r = k
        if letter.upper() not in used_letters:
            for i in range(0, len(secret_word)):
                if letter.upper() == secret_word[i]:
                    result[i] = secret_word[i]
                    k = k+1
            if r == k:
                count = count-1
            print(result)
        used_letters.append(letter.upper())
    proverka(count, secret_word)


def nachalo():
    lst = ['Пикник', 'Дворец', 'Ограда', 'Карниз']
    word = random.choice(lst)
    word = word.upper()
    return word


def shifrovka(secret_word):
    result = []
    for i in range(0, len(nachalo())):
        result.append('_')
    print(result)
    return result


def proverka(count, secret_word):
    if count == 0:
        print('Вы проиграли... Ответ:', secret_word)
    else:
        print('Вы победили')


game()
