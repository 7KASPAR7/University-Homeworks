from caesar_logic import encrypt, decrypt


Button = str(input(' Encrypt text - press E. Decrypt text - press D'))
if Button == 'e' or Button == 'E':
    a = str(input('text:'))
    n = input('offset:')
    try:
        n = int(n)
    except ValueError:
        print('Incorrect input')
    print(encrypt(int(n), a))

elif Button == 'd' or Button == 'D':
    a = str(input('text:'))
    n = input('offset:')
    try:
        n = int(n)
    except ValueError:
        print('Incorrect input')
    print(decrypt(int(n), a))
else:
    raise ValueError('Incorrect Button')
