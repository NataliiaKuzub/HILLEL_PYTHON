word_1 = input("Please, enter the fist word: ").lower()
word_2 = input("Please, enter the second word: ").lower()
count_differ = False

if word_1 == word_2:
    print("This is the same word!")
else:
    set_1 = set([i for i in word_1 if i.isalpha()])
    set_2 = set([i for i in word_2 if i.isalpha()])
    if set_1 == set_2:
        count_differ = True
        for i in set_1:
            if word_1.count(i) != word_2.count(i):
                count_differ = False
                break
    if count_differ:
        print("The words are anagrams!")
    else:
        print("The words are not anagrams!")




