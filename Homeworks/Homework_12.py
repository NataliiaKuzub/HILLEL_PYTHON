text_initial = input("Please, enter the text: ")
character_set = sorted(set([i.lower() for i in text_initial if i.isalpha()]))
for i in character_set:
    print(f"{i}: {text_initial.count(i)}")
