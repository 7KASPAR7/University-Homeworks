from caesar_logic import encrypt, decrypt


Button = input(' Encrypt text - press E. Decrypt text - press D ')
if Button != 'e' and Button != 'E' and Button != 'd' and Button != 'D':
    raise ValueError('Incorrect Button')
else:
    a = input('text:')
    n = input('offset:')
    try:
        if Button == 'e' or Button == 'E':
            print(encrypt(int(n), a))
        else:
            print(decrypt(int(n), a))
    except ValueError:
        print('Incorrect input')
