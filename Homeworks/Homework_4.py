start = int(input('Please, enter the lower limit for prime numbers search: '))
stop = int(input('Please, enter the upper limit for prime numbers search: '))

prime_numbers_counter = 0
while start <= stop:
    delimiters_counter = 0
    number_counter = 1
    while number_counter <= start:
        if start % number_counter == 0:
            delimiters_counter += 1
        number_counter += 1
    if delimiters_counter <= 2:
        print(start)
        prime_numbers_counter += 1
    start += 1
print("There are", prime_numbers_counter, "prime numbers in total.")
