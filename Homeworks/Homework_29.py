def fibonacci_gen(count):
    my_list = [0, 1]
    while count > 0:
        yield my_list[1]
        my_list.append(sum(my_list))
        my_list.pop(0)
        count -= 1


for f in fibonacci_gen(10):
    print(f)
