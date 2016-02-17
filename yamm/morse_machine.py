#!/usr/bin/python3
#__*__ encoding: utf-8


class MorseMachine():

    '''A simple class to write or read a morse code.
    '''

    # the current(2014) international morse code
    __morse_dict = {
        ' ': ' ',
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '..-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '·----',
        '2': '··---',
        '3': '···--',
        '4': '····-',
        '5': '·····',
        '6': '-····',
        '7': '--···',
        '8': '---··',
        '9': '----·',
        '0': '-----',
        '.': '·-·-·-',
        '.': '·-·-·-',
        ',': '--··--',
        '?': '··--··',
        '\'': '·----·',
        '!': '-·-·--',
        '/': '-··-·',
        '(': '-·--·',
        ')': '-·--·-',
        '&': '·-···',
        ':': '----···',
        ';': '-·-·-·',
        '=': '-···-',
        '-': '-····-',
        '_': '··--·-',
        '\"': '·-··-·',
        '$': '···-··-',
        '@': '·--·-·',
        'ä': '·-·-',
        'æ': '·-·-',
        'à ': '·--·-',
        'å ': '·--·-',
        'ç ': '-·-··',
        'ĉ': '-·-··',
        'ch': '----',
        'ð ': '··--·',
        'è ': '·-··-',
        'é ': '··-··',
        'ĝ ': '--·-·',
        'ĥ ': '-·--·',
        'ĵ ': '·---·',
        'ñ ': '--·--',
        'ö ': '---·',
        'ŝ ': '···-·',
        'þ ': '·--··',
        'ü ': '··--',
    }

    def write(self, plaintext):
        ''' encrypt a plaintext '''
        #' '.join([x if x == ' ' else self.__morse_dict[x] for x in plaintext])
        result = []
        plaintext = plaintext.lower()
        for letter in plaintext:
            if letter not in self.__morse_dict.keys():
                result.append('?')
            else:
                result.append(self.__morse_dict[letter])
        return ' '.join(result)

    def read(self, code):
        ''' translate a code in plaintext '''
        blocks = code.split()
        result = []
        for block in blocks:
            # stop if some block is invalid...
            if block not in self.__morse_dict.values():
                return 'Invalid code! =\\'
            else:
                result.append(next((key for key, value in
                                    self.__morse_dict.items() if value == block
                                    )))
        return ' '.join(result)

    @property
    def alphabet(self):
        ''' get all morse dictionary '''
        return self.__morse_dict
