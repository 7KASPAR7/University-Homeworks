from hangman_logic import beginning, encryption, check, gues

count = 5
print('Попыток осталось:', count)
secret_word = beginning()
result = encryption()
used_letters = []
k = 0
while count > 0 and k != len(secret_word):
    r = k
    letter = str(input('Введите букву'))
    if 1040 < ord(letter) < 1104:
        count, k = gues(letter, count, secret_word, result, used_letters, r, k)
    else:
        raise TypeError('Можно вводить только одну букву русского алфавита')
check(count, secret_word)
