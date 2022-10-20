d = {
    "apple": ["malum", "pomum", "popula"],
    "fruit": ["baca", "bacca", "popum"],
    "punishment": ["malum", "multa"]
}

latin_words = []
for i in d.values():
    latin_words.extend(i)

for i in set(latin_words):
    print(f'{i.upper()}:')
    for key in d:
        if i in d[key]:
            print(f'- {key}')

