codec = {
    'a':'.-',
    'b':'-...',
    'c':'-.-.',
    'd':'-..',
    'e':'.',
    'f':'..-.',
    'g':'--.',
    'h':'....',
    'i':'..',
    'j':'.---',
    'k':'-.-',
    'l':'.-..',
    'm':'--',
    'n':'-.',
    'o':'---',
    'p':'.--.',
    'q':'--.-',
    'r':'.-.',
    's':'...',
    't':'-',
    'u':'..-',
    'v':'...-',
    'w':'.--',
    'x':'-..-',
    'y':'-.--',
    'z':'--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    ':': '---...',
    ';': '_._._.',
    "'": '.----.',
    '"': '.-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '/': '-..-.',
    '-': '-....-',
    '=': '-...-',
    '+': '.-.-.',
    '!': '-.-.--',
    '×': '-..-',
    '@': '.--.-.',
    ' ':'/'
}

class Morsepy():

    @staticmethod
    def encrypt(str):
        """
        Encrypts any string into morse 
        Only one string can be passed as an argument
        """

        cipher = ''
        for char in str:
            try:
                cipher += codec[char]
                cipher += ' '
            except KeyError:
                raise ValueError(f' Character "{char}" is not currently supported by morsepy')

        return cipher.strip()

    @staticmethod
    def decrypt(str):
        """
        Decrypts a morse string into english,
        Morse characters should be seperated by spaces and words seperated with a /,
        the / can either be padded by whitespace (e.g ' / ') or not padded by whitespace (e.g '/')
        but the same should be used every time a slash is placed, otherwise a SyntaxError will be raised
        """

        cipher = ''
        wordsplit = ' / ' if ' / ' in str else '/' #determines wether words should be split with / padded by whitespace or / not padded by whitespace
        wordlist = [word.split(' ') for word in str.split(wordsplit)] #gives list of 
        
        #adds letter associated with morse character inside dict
        for charlist in wordlist:
            for char in charlist:
                
                if char not in codec.values():
                    raise SyntaxError(f' Morse character "{char}" does not exist')
                
                for letter, morse in codec.items():
                    if morse == char:
                        cipher += letter

            cipher += ' '

        return cipher.strip()

if __name__ == '__main__':
    #examples of encrypt and decrypt
    print(Morsepy.encrypt('haha, brrr. lmao 1234!!'))
    print(Morsepy.decrypt('.... .- .... .- --..-- / -... .-. .-. .-. .-.-.- / .-.. -- .- --- / .---- ..--- ...-- ....- -.-.-- -.-.--'))

    print(Morsepy.encrypt(input(">>> ")))
