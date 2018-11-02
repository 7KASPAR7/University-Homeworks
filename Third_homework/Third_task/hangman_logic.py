import random


def gues(letter, count, secret_word, result, used_letters, r, k):
    if letter.upper() not in used_letters:
        for i in range(0, len(secret_word)):
            if letter.upper() == secret_word[i]:
                result[i] = secret_word[i]
                k = k+1
        if r == k:
            count = count-1
        print('Попыток осталось:', count)
        print(result)
    used_letters.append(letter.upper())
    return count, k


def beginning():
    lst = ['Пикник', 'Шахта', 'Оградка', 'Пудель', 'Покрывало', 'Броня']
    word = random.choice(lst)
    word = word.upper()
    return word


def encryption(word):
    result = []
    for i in range(0, len(word)):
        result.append('_')
    print(result)
    return result


def check(count, secret_word):
    if count == 0:
        print('Вы проиграли!!! Я выливаю ваше вино в раковину...')
        print('Загаданное слово было:', secret_word)
    else:
        print('Вы победили!!! Моё уважение) Теперь вы можете помыть конус!')
