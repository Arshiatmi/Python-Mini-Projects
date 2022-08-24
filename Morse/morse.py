from enum import Enum
from alphabet import Alphabet


class Mode(Enum):
    nothing = 0
    encrypt = 1
    decrypt = 2


# This Function Will Split A Text With Escape Some Characters
def split(string, delimiter=' ', escape_char='/'):
    temp_text = ""
    splitted_text = []
    counter = 0
    escaping = False
    while counter < len(string):
        if string[counter] == delimiter:
            if escaping:
                temp_text += string[counter]
            else:
                splitted_text.append(temp_text)
                temp_text = ''
        elif string[counter] == escape_char:
            escaping = not escaping
        else:
            temp_text += string[counter]
        counter += 1
    splitted_text.append(temp_text)
    return splitted_text


class Morse:

    def __init__(self, alphabet=Alphabet):
        self.alphabet = alphabet
        self.reverse_alphabet = {value: key for key, value in alphabet.items()}
        self.last_morse = ""
        self.last_mode = Mode.nothing

    @property
    def raw_morse(self):
        return self.last_morse.replace("/ /", "")

    def __call__(self, text, mode=Mode.encrypt):
        answer = ""
        text = text.upper().strip()
        if mode == Mode.encrypt:
            for char in text:
                if char == " ":
                    answer += f" /{char}/ "
                    continue
                try:
                    answer += self.alphabet[char] + " "
                except:
                    answer += char + " "
        elif mode == Mode.decrypt:
            for char in split(text):  # This Custom Split Will Return Morse With Escaped Text
                try:
                    answer += self.reverse_alphabet[char]
                except:
                    answer += char
        else:
            raise ValueError(
                "Unknown Mode. Mode must be Mode.encrypt Or Mode.decrypt.")
        self.last_morse = answer.capitalize()
        self.last_mode = mode
        return self.last_morse

    def get_raw_morse(self):
        return self.last_morse.replace("/ /", "")

    def morse(self, text):
        return self.__call__(text)

    def text(self, text):
        return self.__call__(text, mode=Mode.decrypt)

    def encrypt(self, text):
        return self.__call__(text)

    def decrypt(self, text):
        return self.__call__(text, mode=Mode.decrypt)

    def __len__(self):
        if self.last_mode == Mode.encrypt:
            return len(self.last_morse.split())
        elif self.last_mode == Mode.decrypt:
            return len(self.last_morse)
        else:
            return -1

    def __str__(self):
        return self.get_raw_morse()

    def __repr__(self):
        return self.get_raw_morse()
