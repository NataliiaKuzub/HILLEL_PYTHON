text_initial = input("Enter the text, please: ")
text_corrected = ""
for i in range(len(text_initial)):
    if i % 2 == 0:
        text_corrected += text_initial[i].upper()
    else:
        text_corrected += text_initial[i].lower()
print(text_corrected)
