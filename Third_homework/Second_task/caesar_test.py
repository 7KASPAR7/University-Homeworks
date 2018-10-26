from unittest import TestCase, main
from caesar_logic import encrypt, decrypt


class Value_Tests(TestCase):
    def Encrypts_Values(self):
        self.assertEqual(encrypt(8, 'Hello world!'), 'Pmttw ewztl!')
        self.assertEqual(encrypt(0, 'Hello world!'), 'Hello world!')
        self.assertEqual(encrypt(-28, 'Hello world!'), 'Fcjjm umpjb!')

    def Decrypts_Values(self):
        self.assertEqual(decrypt(-28, 'Fcjjm umpjb!'), 'Hello world!')
        self.assertEqual(decrypt(0, 'Hello world!'), 'Hello world!')
        self.assertEqual(decrypt(8, 'Pmttw ewztl!'), 'Hello world!')


main()
