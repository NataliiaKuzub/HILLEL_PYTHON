valid = False
while not valid:
    try:
        children = int(input("How many children are there? "))
        apples = int(input("How many apples do you have? "))
        valid = True
    except ValueError:
        print("Please, enter only whole numbers!")

print("Each child will get", apples // children, "apples.")
print(apples % children, "apples will remain.")
