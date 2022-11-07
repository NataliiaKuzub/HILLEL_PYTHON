int_list = [int(i) for i in input('Please, enter the numbers, separated by comma: ').split(',')]

mean_list = []
for i in range(1, len(int_list) + 1):
    if i < 7:
        mean_list.append(round(sum(int_list[:i])/i, 1))
    else:
        mean_list.append(round(sum(int_list[i-7:i])/7, 1))
print(mean_list)
