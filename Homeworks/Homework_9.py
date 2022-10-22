wealth = (input("Please, enter the salaries of the people separated by coma: "))
wealth_list = [int(i) for i in wealth.split(", ")]
print("A silver spoons:")
for i in range(1, len(wealth_list)-1):
    if wealth_list[i] > wealth_list[i - 1] + wealth_list[i + 1]:
        print(f"{i + 1}. {wealth_list[i]}")
