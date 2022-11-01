int_list = [int(i) for i in input("Please, enter the list of integers to inspect divided by coma: ").split(',')]

counter = 0
i = 0

while i < len(int_list):
    if int_list[i] % 2 == 0:
        pre_counter = 0
        while i < len(int_list) and int_list[i] % 2 == 0:
            i += 1
            pre_counter += 1
        counter = pre_counter if pre_counter > counter else counter
    else:
        i += 1

print(f"The biggest count of even numbers in a row is {counter}")





