def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


limits = input("Please, enter lower and upper limits separated by coma: ")
limits = [int(i) for i in limits.split(",")]

pn_counter = 0
for i in range(limits[0], limits[1] + 1):
    if is_prime(i):
        pn_counter += 1
        print(i)
print(f"There are {pn_counter} prime numbers in total.")
