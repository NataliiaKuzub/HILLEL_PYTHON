text_initial = input("Enter the text please: ")
text_corrected = ""
for i in range(len(text_initial)):
    if text_initial[i] != " " or text_initial[i - 1] != " ":
        text_corrected += text_initial[i]
print(text_corrected)
