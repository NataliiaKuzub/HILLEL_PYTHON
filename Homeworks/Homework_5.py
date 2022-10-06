answer = input("Buy an elephant! ")
while True:
    if answer == "already bought":
        print("Great!")
        break
    else:
        answer = input('Everybody saying "' + answer + '", but you buy an elephant! ')