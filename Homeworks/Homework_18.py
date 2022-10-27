text = input("Please, enter christmas text: ")

center_pos = int(len(text)/2)

start = center_pos - 1
if len(text) % 2 == 0:
    stop = center_pos + 1
else:
    print(text[center_pos].center(len(text)))
    stop = center_pos + 2

while start > 0:
    print(text[start:stop].center(len(text)))
    start -= 1
    stop += 1

print(text)
