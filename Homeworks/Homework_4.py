start = int(input('Please, enter the lower limit for prime numbers search: '))
stop = int(input('Please, enter the upper limit for prime numbers search: '))

prime_numbers_counter = 0
print("Here the prime numbers in the specified range:")

while start <= stop:
    is_prime = True
    number_counter = 2

    while number_counter < start:

        if start % number_counter == 0:
            is_prime = False
            break
        number_counter += 1

    if is_prime:
        print(start)
        prime_numbers_counter += 1

    start += 1

print("There are", prime_numbers_counter, "prime numbers in total.")
