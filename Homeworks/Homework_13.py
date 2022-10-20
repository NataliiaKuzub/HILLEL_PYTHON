morse_dict = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z'
}

text = input('Please, enter the signal: ').split('    ')
text = [word.split(' ') for word in text]

for word_position, word in enumerate(text):
    for letter_position, letter in enumerate(word):
        word[letter_position] = morse_dict.get(letter, '~')
    text[word_position] = ''.join(word)
print(f"Corresponding english text: {' '.join(text)}")

