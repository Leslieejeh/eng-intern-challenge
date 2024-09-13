import sys

# Solution to brallie challenge 
#  A dictionary of the braile to english 
# A method that accepts the converting string 
# remeber if we know A to j we already know most of all the other characters
# This condition doesnt apply to numbers and punctuation marks 

english_to_braille = {
    'a': 'O.....',  # A
    'b': 'O.O...',  # B
    'c': 'OO....',  # C
    'd': 'OO.O..',  # D
    'e': 'O..O..',  # E
    'f': 'OOO...',  # F
    'g': 'OOOO..',  # G
    'h': 'O.OO..',  # H
    'i': '.OO...',  # I
    'j': '.OOO..',  # J
    'k': 'O...O.',  # K
    'l': '0.O.O.',  # L
    'm': 'OO..O.',  # M
    'n': 'OO.OO.',  # N
    'o': 'O..OO.',  # O
    'p': 'OOO.O.',  # P
    'q': 'OOOOO.',  # Q
    'r': 'O.OOO.',  # R
    's': '.OO.O.',  # S
    't': '.OOOO.',  # T
    'u': 'O...OO',  # U
    'v': 'O.O.OO',  # V
    'w': '.OOO.O',  # W special character 
    'x': 'OO..OO',  # X
    'y': 'OO.OOO',  # Y
    'z': 'O..OOO',  # Z

  

    # Numbers, prefixed by a number sign
    '1': 'O.....',  # 1 (same as 'a')
    '2': 'O.O...',  # 2 (same as 'b')
    '3': 'OO....',  # 3 (same as 'c')
    '4': 'OO.O..',  # 4 (same as 'd')
    '5': 'O..O..',  # 5 (same as 'e')
    '6': 'OOO...',  # 6 (same as 'f')
    '7': 'OOOO..',  # 7 (same as 'g')
    '8': 'O.OO..',  # 8 (same as 'h')
    '9': '.OO...',  # 9 (same as 'i')
    '0': '.OOO..',  # 0 (same as 'j')

    # Special symbols (need sortting )
    ' ': '......',  # Space
    '.': '.O..OO',  # Period
    ',': '.O....',  # Comma
    '?': '.O...O',  # Question mark
    '!': '.OO.O.',  # Exclamation mark
    ':': '.O..O.',  # Colon
    ';': '.OO...',  # Semicolon
    '-': '..O..O',  # Dash
    '/': '..OO..',  # Slash
    '<': 'O..O.O',  # Less than
    '>': '....OO',  # Greater than
    '(': 'OO...O',  # Left parenthesis
    ')': '..O.OO',  # Right parenthesis

}
char_num_punct={
    'capital_follows': '.....O',  # Capital follows (dot 6)
    'decimal_follows': '.O...O',  # Decimal follows (dots 4, 6)
    'number_follows': '.O.O0O',   # Number follows (dots 3, 4, 5, 6)
}

braille_to_eng = {v: k for k, v in english_to_braille.items()}
brl_to_num = {
    'O.....': '1', 'O.O...': '2', 'OO....': '3', 'OO.O..': '4', 'O..O..': '5',
    'OOO...': '6', 'OOOO..': '7', 'O.OO..': '8', '.OO...': '9', '.OOO..': '0',
}

# braille_to_english = {
#     'O.....': 'a',  # Braille for 'a'
#     'OO....': 'b',  # Braille for 'b'
#     'O.O...': 'c',  # Braille for 'c'
#     'O..OO.': 'd',  # Braille for 'd'
#     'O...O.': 'e',  # Braille for 'e'
#     # Add the rest of the alphabet

#     # Numbers, prefixed by a number sign (handled separately)
#     'O.....': '1',  # Braille for '1'
#     'OO....': '2',  # Braille for '2'
#     # Add more numbers

#     # Special symbols
#     '......': ' ',  # Space
#     '.O..OO': '.',  # Period
#     '.O....': ',',  # Comma
#     '.O...O': '?',  # Question mark
#     # Add more punctuation
# }



# Top method that controls if its a text or in braille and delegates a fucntion to carry out the task of translation 
def Translate(text):
    # Check if the first character equals to a dot (need to revise this logic)
    if text[0]== '.':
        Braille_to_english(text)
    else:
        Translate_to_english(text)

def Translate_to_english(text):
    braille=''
    for i in range(0, len(text)):
        # Track previous char incase we need to switch 
        current_char = text[i]
        previous_char = text[i-1] if i > 0 else '' 

        if current_char.isupper():
            print(current_char)
            braille+=char_num_punct['capital_follows']
            # converting to lower because it doesnt have capital letters in the dictionary 
            braille+=english_to_braille[current_char.lower()]
        elif current_char== ' ':
            print(current_char)
            braille+=english_to_braille[current_char.lower()]
        elif current_char.isdigit():
            print(current_char)
            # Check if the previous character is not a digit or space to add 'number_follows'
            if previous_char == '' or not previous_char.isdigit():
                braille += char_num_punct['number_follows']
            # add the braille for the current digit
            braille += english_to_braille[current_char]
        else:
            print(current_char)
            braille+=english_to_braille[text[i].lower()]       
    print(braille)

def Braille_to_english(text):
    english_text = ''
    chunks = [text[i:i+6] for i in range(0, len(text), 6)]
    is_number = False
    is_capital = False

    for braille in chunks:
        # Check for number indicator
        if braille == char_num_punct['number_follows']:
            is_number = True
            continue

        # Check for space
        if braille == '......':
            english_text += ' '
            is_number = False
            is_capital = False
            continue

        # Check for capital indicator
        if braille == char_num_punct['capital_follows']:
            is_capital = True
            continue

        # Handle numbers if number flag is set
        if is_number:
            if braille in brl_to_num:
                english_text += brl_to_num[braille]
            continue

        # Handle letters and capital letters
        if braille in braille_to_eng:
            if is_capital:
                english_text += braille_to_eng[braille].upper()
                is_capital = False
            else:
                english_text += braille_to_eng[braille]


    print(english_text)
  


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text_to_translate>")
    else:
        input_text = ' '.join(sys.argv[1:])  # Join all arguments into one string
        result = Translate(input_text)
    