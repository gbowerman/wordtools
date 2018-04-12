'''morse.py - ascii to Morse code conversion tool'''
import sys

# alphabet lookup table, e.g. A = alphabet[0], Z = alphabet[25]
letters = ['· –', '– · · ·', '– · – ·', '– · ·', '·', '· · – ·', '– – ·', '· · · ·', '· ·',
            '· – – –', '– · –', '· – · ·', '– –', '– ·', '– – –', '· – – ·', '– – · –', '· – ·',
            '· · ·', '–', '· · –', '· · · –', '· – –', '– · · –', '– · – –', '– – · ·']

# digit lookup table 0-9, e.g. 0 = digits[0], 9 = digits[9]
digits = ['– – – – –', '· – – – –', '· · – – –', '· · · – –', '· · · · –', '· · · · ·',
           '– · · · ·', '– – · · ·', '– – – · ·', '– – – – ·']

def convert_to_morse(alphastring):
    '''Takes an alphanumeric string and converts it to a Morse string'''
    output_string = ''
    for ch in alphastring.upper():
        if ch.isspace():
            output_string += '\n'
            continue
        elif ch.isalpha():
            numval = ord(ch) - 65
            output_string += letters[numval]
        elif ch.isdigit():
            numval = ord(ch) - 48
            output_string += digits[numval]
        output_string += '   '
    return output_string

if __name__ == "__main__":
    morse_str = convert_to_morse(sys.argv[1])
    print(morse_str)

