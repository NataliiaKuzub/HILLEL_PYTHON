file_name = input("Please, enter the file name: ")
word_dict = {}

with open(file_name, encoding='utf-8') as f:
    for line in f.readlines():
        word = ''
        for i in line:
            if i.isalpha():
                word += i
            else:
                if len(word) >= 5:
                    if word.lower() in word_dict.keys():
                        word_dict[word.lower()] += 1
                    else:
                        word_dict[word.lower()] = 1
                word = ''

print('The top used words in the given text are:')
for i in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(i[0], i[1])
