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

morse_list = input('Please, enter the signal: ').split('    ')
morse_list = [i.split(' ') for i in morse_list]
english_list = []

for i in morse_list:
    word = ""
    for letter in i:
        word += morse_dict.get(letter, '~')
    english_list.append(word)

print(f"Corresponding english text: {' '.join(english_list)}")


