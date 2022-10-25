def is_prime(number):
    check_prime = True
    for i in range(2, number):
        if number % i == 0:
            check_prime = False
            break
    return check_prime


limits = input("Please, enter lower and upper limits separated by coma: ")
limits = [int(i) for i in limits.split(",")]

pn_counter = 0
for i in range(limits[0], limits[1] + 1):
    if is_prime(i):
        pn_counter += 1
        print(i)
print(f"There are {pn_counter} prime numbers in total.")
