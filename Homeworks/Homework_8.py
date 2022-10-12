text_initial = input("Enter the text, please: ")
text_bolgarica = (
    text_initial
    .replace("З", "3")
    .replace("О", "0")
    .replace("и", "u")
    .replace("п", "n")
    .replace("т", "m")
    .replace("к", "k")
    .replace("д", "g")
)
print(text_bolgarica)
