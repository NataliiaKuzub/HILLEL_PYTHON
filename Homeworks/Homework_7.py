text_initial = input("Enter the text, please: ")
text_corrected = ""
for i in range(len(text_initial)):
    text_corrected += text_initial[i].upper() if i % 2 == 0 else text_initial[i].lower()
print(text_corrected)
