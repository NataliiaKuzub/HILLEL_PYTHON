text_list = list(input("Enter the text for correction: "))
k = -1
i = 0
while "," in text_list[k+1:]:
    k = text_list.index(",", k + 1)
    i += 1
    if i % 3 == 0:
        text_list.insert(k, " huck")
        k += 1
print("".join(text_list))
